from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

#Modelagem do banco de dados
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Router(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False, unique=True)
    link = db.Column(db.String(100), nullable=False, unique=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET'])
def pagina_login():
    return render_template('login.html')

#Autenticação
@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('dashboard'))
    
    flash('Email ou senha incorretos.', 'error')
    return redirect(url_for('pagina_login'))

@app.route('/logout', methods = ['POST'])
@login_required
def logout():
    logout_user()
    return jsonify ({"message": "Deslogado com sucesso!"})

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if len(password) < 4:
        flash('A senha deve ter pelo menos 4 caracteres.', 'error')
        return redirect(url_for('register'))
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash('Endereço de email inválido.', 'error')
        return redirect(url_for('register'))

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email já cadastrado.', 'error')
        return redirect(url_for('register'))

    if username and email and password:
        user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso! Você já pode efetuar o Login.', 'success')
        return redirect(url_for('pagina_login'))
    
    flash('Por favor, preencha todos os campos.', 'error')
    return redirect(url_for('register'))

@app.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)