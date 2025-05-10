import os
from flask import (Flask,
                    jsonify,
                    redirect,
                    request,
                    render_template,
                    url_for
                    )

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "notes.sqlite")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"


# HOME
@app.route("/")
def home():
    """role= "admin2s"
    notes = ["Note 1", "Note 2", "Note 3"]
    data = {
        "titulo": "nota1",
        "contenido": "contenido de la nota",
        "fecha": "12/02/2025",
    }
    notes = [
        {"title": "Título de prueba", "content": "Contenido de prueba",}
    ]
    return render_template("home.html", role=role, notes=notes, data=data)"""
    notes = Note.query.all()  # Obtiene tods las notas de la base de datos
    return render_template("home.html", notes=notes)


@app.route("/acerca-de")
def acerca_de():
    return "Esto es una App de Notas."


@app.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctanente", 201
    return "Pagina de contacto"


@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version:": "1.1.1",
    }
    return jsonify(data), 200


@app.route("/confirmacion")
def confirmation():
    note = request.args.get("note", "No encontrada.")
    print(note)
    return render_template("confirmation.html", note=note)


# NOTE CREATION
@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        note_db = Note(title=title, content=content)
        db.session.add(note_db)
        db.session.commit()
        return redirect(url_for("confirmation"))
    return render_template("note_form.html")


# EDIT NOTE
@app.route("/editar-nota/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.title = request.form.get("title")
        note.content = request.form.get("content")

        db.session.commit()
        return redirect(url_for("home"))
    return render_template("note_form.html", note=note)


@app.route("/eliminar-nota/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("home"))
