from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e040592789b71d4d66fa87839be22de9'

basedir = os.path.abspath(os.path.dirname(__file__))  # Get the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "site.db")}'
db = SQLAlchemy(app)

from flaskblog import routes