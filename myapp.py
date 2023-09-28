from flask import Flask, request, make_response, url_for
from flask import render_template, redirect, session
from markupsafe import escape
import secrets
from flask_sqlalchemy import SQLAlchemy
from models import db, User
import docker
from MyContainer import MyContainer
from datetime import datetime
import asyncio

app = Flask(__name__)
app.secret_key = secrets.token_hex()
client = docker.from_env()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:6444/flask'
db.init_app(app)
client = docker.from_env()
obj = MyContainer()

# db = SQLAlchemy(app)

@app.get('/')
def index_get():
    return render_template('index.html')

@app.post('/')
def index_post():
    first_name = escape(request.form.get('firstName'))
    second_name = escape(request.form.get('secondName'))
    email = escape(request.form.get('email'))
    password = escape(request.form.get('password'))
    user = User(first_name, second_name, email, password)
    db.session.add(user)
    db.session.commit()
    print(user)
    return render_template('index.html')

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("start-ct")
def start_ct():
    asyncio.run(obj.starter())
    db.create_all()
    print('OK')



if __name__ == '__main__': 
    app.run(debug=True)