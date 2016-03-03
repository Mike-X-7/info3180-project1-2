from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pbcxcvuyoyrzgs:p86wdUF7ajFqWA8kMem_qLcnIf@ec2-54-197-238-19.compute-1.amazonaws.com:5432/dbcgn7dkditdsb'
db = SQLAlchemy(app)

from app import views, models

# The app didn't write to my database(the link above) I got an error when running the "heroku run init" statement.
# however, i tryed to link another database to the app and it WORKED PERFECTLY.
# someone else's database i tried, worked:   postgres://nuvvubrysbqmrz:QjhlkvAnHI8QY_RETj76R8Q63-@ec2-23-21-219-209.compute-1.amazonaws.com:5432/d8rqq5trvho033
