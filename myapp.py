from flask import Flask, request, make_response, url_for
from flask import render_template, redirect, session
from markupsafe import escape
import secrets
from flask_sqlalchemy import SQLAlchemy
from models import db, User
import docker

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@172.20.10.2:6432/bank'
db.init_app(app)
client = docker.from_env()

# db = SQLAlchemy(app)

@app.get('/')
def index_get():
    # name = request.cookies.get('username')
    # print(f'Hello {name}!')
    postgrContainer = client.containers.get('09548287cc8e')
    # container = client.containers.run('hello-world', detach=True)
    # container1 = client.containers.get('raftest')
    print(postgrContainer.labels)
    # print(client.)
    print(client.containers.list())
    return render_template('index.html')

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

if __name__ == '__main__': 
    app.run(debug=True)