from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ivezcfmrudhirt:jhNai6vB3aFIYkenXB3cREcKqn@ec2-107-21-229-87.compute-1.amazonaws.com:5432/da6pgt9pupus5n'
db = SQLAlchemy(app)

from app import views, models

#