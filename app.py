from flask import Flask, request
from config import Config
from models import db
from flask_migrate import Migrate
from notes.routes import notes_bp
from users.routes import users_bp
from auth.routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(notes_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    migrate = Migrate(app, db) # <--- Añade esta línea   

    @app.route("/acerca-de")
    def acerca_de():
        return "Esto es una App de Notas."


    @app.route("/contacto", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            return "Formulario enviado correctanente", 201
        return "Pagina de contacto"

    return app