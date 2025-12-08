from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import os, re, requests
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
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

class Router(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    local = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False, unique=True)
    link = db.Column(db.String(100), nullable=False)
    link1 = db.Column(db.String(100))
    link2 = db.Column(db.String(100))


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
    return redirect(url_for('pagina_login'))

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
    routers = Router.query.all()
    return render_template('dashboard.html', routers=routers)

@app.route('/add_router', methods = ['GET', 'POST'])
@login_required
def add_router():
    if not current_user.is_admin:
        flash('Acesso negado. Apenas administradores podem adicionar roteadores.', 'error')
        return redirect(url_for('dashboard'))

    local = request.form.get('local')
    model = request.form.get('model')
    serial = request.form.get('serial')
    link = request.form.get('link')
    link1 = request.form.get('link1')
    link2 = request.form.get('link2')

    router = Router.query.filter_by(serial=serial).first()
    if router:
        flash('Roteador já cadastrado.', 'error')
        return redirect(url_for('dashboard'))
    
    if local and model and serial and link:
        router = Router(local=local, model=model, serial=serial, link=link, link1=link1, link2=link2)
        db.session.add(router)
        db.session.commit()
        return redirect(url_for('dashboard'))
    
@app.route('/delete', methods = ['POST'])
@login_required
def delete():
    if not current_user.is_admin:
        flash('Acesso negado. Apenas administradores podem deletar roteadores.', 'error')
        return redirect(url_for('dashboard'))

    router_id = request.form.get('id')
    Router.query.filter_by(id=router_id).delete()
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/check_status/<int:router_id>')
@login_required
def check_status(router_id):
    router = Router.query.get_or_404(router_id)
    url = router.link
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        response = requests.get(url, timeout=3)
    
        if response.status_code == 200 or response.status_code == 401:
            return jsonify({'status': 'online'})
        else:
            return jsonify({'status': 'warning'})
    except requests.RequestException:
        return jsonify({'status': 'offline'})

@app.route('/settings', methods = ['GET'])
@login_required
def settings():
    return render_template('settings.html')

@app.route('/new_password', methods = ['POST'])
@login_required
def new_password():

    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not password or len(password) < 4:
        flash('A senha deve ter pelo menos 4 caracteres.', 'error')
        return redirect(url_for('settings'))

    if password != confirm_password:
        flash('As senhas não coincidem!', 'error')
        return redirect(url_for('settings'))

    try:
        current_user.password = generate_password_hash(password)
        db.session.commit()
        flash ('A sua senha foi alterada com sucesso!', 'success')
        return redirect(url_for('settings'))
    
    except:
        db.session.rollback()
        flash ('Erro ao salvar nova senha.', 'error')
        return redirect(url_for('settings'))
    
@app.route('/dashboard_admin', methods = ['GET'])
@login_required
def dashboard_admin():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))

    users = User.query.all()
    return render_template('admin_dashboard.html', users = users)

@app.route('/add_user', methods = ['POST'])
@login_required
def add_user():
    if not current_user.is_admin:
        return redirect(url_for('dashboard'))

    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    is_admin = request.form.get('is_admin') == '1'

    if len(password) < 4:
        flash('A senha deve ter pelo menos 4 caracteres.', 'error')
        return redirect(url_for('dashboard_admin'))

    user = User.query.filter_by(email = email).first()
    if user:
        flash('Usuário já cadastrado.', 'error')
        return redirect(url_for('dashboard_admin'))
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash('Endereço de email inválido.', 'error')
        return redirect(url_for('dashboard_admin'))

    if username and email and password:
        user = User(username = username, email = email, password = password, is_admin = is_admin)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('dashboard_admin'))
    
    flash('Preencha todos os campos obrigatórios', 'error')
    return redirect(url_for('dashboard_admin'))

@app.route('/delete_user', methods = ['POST'])
@login_required
def delete_user():
    if not current_user.is_admin:
        flash('Acesso negado. Apenas administradores podem deletar usuários.', 'error')
        return redirect(url_for('dashboard'))
    
    user_id = request.form.get('id')

    if str(current_user.id) == str(user_id):
        return redirect(url_for('dashboard_admin'))

    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect(url_for('dashboard_admin'))

if __name__ == '__main__':
    app.run(debug=True)