from flask import Flask, request, make_response, url_for
from flask import render_template, redirect, session
from markupsafe import escape
import secrets
from flask_sqlalchemy import SQLAlchemy
from models import db, Myuser
import docker

app = Flask(__name__)
app.secret_key = secrets.token_hex()
client = docker.from_env()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:6444/flask'
db.init_app(app)
client = docker.from_env()

@app.get('/')
def index_get():
    # name = request.cookies.get('username')
    # print(f'Hello {name}!')
    # postgrContainer = client.containers.get('09548287cc8e')
    # container = client.containers.run('hello-world', detach=True)
    # container1 = client.containers.get('raftest')
    # print(postgrContainer.labels)
    # print(client.)
    # print(client.containers.list())
    return render_template('index.html')

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("start-ct")
def start_ct():
    ports = {'5432/tcp': 6444}
    environment={"POSTGRES_USERNAME":"postgres", "POSTGRES_PASSWORD": "postgres", "POSTGRES_DB": "flask"}
    container = client.containers.run('postgres:15.4', ports=ports, environment=environment, detach=True)
    print('OK')

if __name__ == '__main__': 
    app.run(debug=True)
