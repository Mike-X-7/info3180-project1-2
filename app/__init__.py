from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bmniivoamllwmw:RwyGm7VWY0_LkTdDAQgTT7biQq@ec2-54-83-3-38.compute-1.amazonaws.com:5432/d16qhmq0uetl5u'
db = SQLAlchemy(app)

from app import views, models

#