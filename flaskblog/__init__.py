from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

with open('config.json', 'r') as f:
  config = json.load(f)

app.config['SECRET_KEY'] = config['APP_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URI']

db = SQLAlchemy(app)


from flaskblog import routes
