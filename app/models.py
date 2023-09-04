from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdcarsales.db'
#db = SQLAlchemy(app)

#class Autos(db.model):
class Autos(db.Model):

    idauto =db.Column(db.Integer,primary_key=True)

    nombre=db.Column(db.String())

    detalle=db.Column(db.Text)

    imagen=db.Column(db.String())

    precio=db.Column(db.Numeric(7,2))

    estado=db.Column(db.Boolean())