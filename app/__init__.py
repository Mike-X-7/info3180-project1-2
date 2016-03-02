from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fdmbbcjwshehwk:mkAURJeFR1hjyrYJpVv6eH_hqT@ec2-54-227-250-148.compute-1.amazonaws.com:5432/dhkdfdno6nhlm'
db = SQLAlchemy(app)

from app import views, models

#