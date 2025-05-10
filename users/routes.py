from flask import Blueprint, render_template, request, redirect, url_for
from models import User, db

users_bp = Blueprint('users', __name__)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica de inicio de sesión
    return render_template('login.html')

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Lógica de registro
    return render_template('register.html')