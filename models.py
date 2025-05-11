
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=True)
    # tiene que aceptar nulo pq existen registros

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=True) # tiene que aceptar nulo pq existen registros

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"