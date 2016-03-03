from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/project1_2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nlbzzrqvfqagmf:gLnCtdKL2_OGrt5en3ndU37NfY@ec2-54-227-246-11.compute-1.amazonaws.com:5432/dfbsdm5e444db9'
db = SQLAlchemy(app)

from app import views, models

#