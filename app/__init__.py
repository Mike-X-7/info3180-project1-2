from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ktnxashaxaxmqu:w7VS3xc-W0rKuRaCTZacxnmqwz@ec2-54-227-250-148.compute-1.amazonaws.com:5432/d94lkdg4cl2h6m'
db = SQLAlchemy(app)

from app import views, models

#