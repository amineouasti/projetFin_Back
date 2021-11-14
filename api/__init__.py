
from flask import Flask,request
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

#import api.users
app = Flask(__name__,static_url_path='',static_folder='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:amine@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']="testSecurite"
db= SQLAlchemy(app)
api = Api(app)



