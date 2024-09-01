from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializar o app Flask
app = Flask(__name__)

# Configurações de conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:SENHAFORTE@ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com/verceldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)

# Modelos (tabelas) do banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

class Processo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processo = db.Column(db.String(255), nullable=False)
    data = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    datapost = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Função para criar as tabelas no banco de dados
def create_tables():
    with app.app_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")

# Função para inserir um usuário
def insert_user(user):
    with app.app_context():
        db.session.add(user)
        db.session.commit()
        print("Usuário inserido com sucesso!")

# Função para inserir um processo
def insert_processo(proc):
    with app.app_context():
        db.session.add(proc)
        db.session.commit()
        print("Processo inserido com sucesso!")

# Função para inserir um post
def insert_post(post):
    with app.app_context():
        db.session.add(post)
        db.session.commit()
        print("Post inserido com sucesso!")

# Funções para seleção de dados
def select_users():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}")

def select_processos():
    with app.app_context():
        processos = Processo.query.all()
        for proc in processos:
            print(f"ID: {proc.id}, Processo: {proc.processo}, Data: {proc.data}")

def select_posts():
    with app.app_context():
        posts = Post.query.all()
        for post in posts:
            print(f"ID: {post.id}, Título: {post.title}, Conteúdo: {post.content}, Data: {post.datapost}, User_id: {post.user_id}")

# Execução
if __name__ == "__main__":
    create_tables()

    # Inserção de dados
    user = User(name="Aluno nota 10", email="alunonota10@example.com")
    insert_user(user)

    proc = Processo(processo="Processo 1", data="01/01/2021", descricao="Teste", status=True)
    insert_processo(proc)

    post = Post(title="Post 2", content="Esse dia foi louco", user_id=1, status=True, datapost="01/01/2021")
    insert_post(post)

    # Seleção e exibição de dados
    select_users()
    select_processos()
    select_posts()
