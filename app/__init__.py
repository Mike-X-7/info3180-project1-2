from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gtjdwpoubkmrbc:se10FLlkNdzGTH1zYIrCNW6Mni@ec2-107-20-148-211.compute-1.amazonaws.com:5432/d616lf8md5jacd'
db = SQLAlchemy(app)

from app import views, models

