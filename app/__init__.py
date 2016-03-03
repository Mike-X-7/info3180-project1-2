from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pbcxcvuyoyrzgs:p86wdUF7ajFqWA8kMem_qLcnIf@ec2-54-197-238-19.compute-1.amazonaws.com:5432/dbcgn7dkditdsb'
db = SQLAlchemy(app)

from app import views, models

#