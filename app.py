from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os
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


#Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods = ['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get("email")).first()

    if user and check_password_hash(user.password, data.get("password")):
        login_user(user)
        return jsonify ({"message": "Logado com sucesso!"})
    
    return jsonify ({"messagge": "Credenciais invalidas."}), 401

@app.route('/logout', methods = ['POST'])
@login_required
def logout():
    logout_user()
    return jsonify ({"message": "Deslogado com sucesso!"})

@app.route('/register', methods = ['POST'])
def register():
    data = request.json
    user = User.query.filter_by(email=data.get("email")).first()
    if user:
        return jsonify ({"message": "Essa conta já existe!"}), 409

    if 'username' in data and 'email' in data and 'password' in data:
        user = User(username=data["username"], email=data["email"], password=generate_password_hash(data["password"]))
        db.session.add(user)
        db.session.commit()
        return jsonify ({"message": "Conta criada com sucesso!"})


if __name__ == '__main__':
    app.run(debug=True)