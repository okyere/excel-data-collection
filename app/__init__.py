# -*- coding: utf-8 -*-
from flask import Flask, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import basedir, UPLOAD_FOLDER
#from flask.ext.mail import Mail

theapp = Flask(__name__)
theapp.config.from_object('config')

#mail = Mail(theapp)
bootstrap = Bootstrap(theapp)

db = SQLAlchemy(theapp)

from app import views, models
