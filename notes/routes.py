from flask import Blueprint, flash, redirect, request, render_template, url_for
from models import Note, db

notes_bp = Blueprint("notes", __name__)


# HOME
@notes_bp.route("/")
def home():
    notes = Note.query.all()  # Obtiene tods las notas de la base de datos
    return render_template("home.html", notes=notes)

# NOTE CREATION
@notes_bp.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        note_db = Note(title=title, content=content)
        db.session.add(note_db)
        db.session.commit()
        flash("Nota creada correctamente", "success")
        return redirect(url_for("notes.home"))
    return render_template("note_form.html")


# EDIT NOTE
@notes_bp.route("/editar-nota/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == "POST":
        note.title = request.form.get("title")
        note.content = request.form.get("content")

        db.session.commit()
        return redirect(url_for("notes.home"))
    return render_template("note_form.html", note=note)


@notes_bp.route("/eliminar-nota/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("notes.home"))