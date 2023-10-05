import psycopg2

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Processo:
    def __init__(self, id, processo, data, descricao, status):
        self.id = id
        self.processo = processo
        self.data = data
        self.descricao = descricao
        self.status = status

class Post:
    def __init__(self, id, title, content, user_id, status, data):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.status = status
        self.datapost = data

def create_table():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Cria a tabela
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
        print("Tabela criada com sucesso!")

        # Cria a tabela
        x = conn.cursor()
        x.execute("""
            CREATE TABLE IF NOT EXISTS processos (
                id SERIAL PRIMARY KEY,
                processo VARCHAR(255) NOT NULL,
                data VARCHAR(255) NOT NULL,
                descricao VARCHAR(255) NOT NULL,
                status BOOLEAN NOT NULL
            )
        """)
        conn.commit()
        print("Tabela Processo criada com sucesso!")

        # Cria a tabela post
        y = conn.cursor()
        y.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                datapost VARCHAR(255) NOT NULL,
                content VARCHAR(255) NOT NULL,
                status BOOLEAN NOT NULL,
                user_id INTEGER NOT NULL
            )
        """)
        conn.commit()
        print("Tabela Post criada com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao criar tabela:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_user(user):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
        conn.commit()
        print("Usuário inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir usuário:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_processo(proc):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO processos (processo, data, descricao, status) VALUES (%s, %s, %s, %s)", (proc.processo, proc.data, proc.descricao, proc.status))
        conn.commit()
        print("Processo inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir processo:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def insert_post(post):
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Insere o usuário na tabela
        cur = conn.cursor()
        cur.execute("INSERT INTO posts (title, datapost, content, status, user_id) VALUES (%s, %s, %s, %s, %s)", (post.title, post.datapost, post.content, post.status, post.user_id))
        conn.commit()
        print("Post inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir post:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_users():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            user = User(row[0], row[1], row[2])
            print(f"ID: {user.id}, Nome: {user.name}, Email: {user.email}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

def select_posts():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            post = Post(row[0], row[1], row[2], row[3], row[4], row[5])
            print(f"ID: {post.id}, Conteúdo: {post.content}, Data: {post.datapost}, Status: {post.status}, User_id: {post.user_id}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()


def select_processos():
    try:
        # Conecta no banco de dados
        conn = psycopg2.connect(
            host="ep-fancy-frog-58641694-pooler.us-east-1.postgres.vercel-storage.com",
            database="verceldb",
            user="default",
            password="9gx0ktdnaVZI"
        )

        # Seleciona todos os usuários da tabela
        cur = conn.cursor()
        cur.execute("SELECT * FROM processos")
        rows = cur.fetchall()

        # Exibe os usuários na tela
        for row in rows:
            proc = Processo(row[0], row[1], row[2], row[3], row[4])
            print(f"ID: {user.id}, Processo: {proc.descricao}, Data: {proc.data}")

    except psycopg2.Error as e:
        print("Erro ao selecionar usuários:", e)

    finally:
        # Fecha a conexão
        if conn is not None:
            conn.close()

# Cria a tabela
create_table()

# Insere um usuário
user = User(None, "ciervo", "ciervo@example.com")
insert_user(user)

# id, processo, data, descricao, status
proc = Processo(None, "Processo 1", "01/01/2021", "Teste", True)
insert_processo(proc)

# self, id, title, content, user_id, status, data):
post = Post(None, "Post 1", "Esse dia foi louco",1, True, "01/01/2021")
insert_post(post)

# Seleciona todos os usuários e exibe na tela
select_users()
select_processos()
select_posts()
