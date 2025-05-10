from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import Note, db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# HOME
@app.route("/")
def home():
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



# NOTE CREATION
@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        note_db = Note(title=title, content=content)
        db.session.add(note_db)
        db.session.commit()
        return redirect(url_for("home"))
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
