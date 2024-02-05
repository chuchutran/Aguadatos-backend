import json 

from db import db
# import models later

import datetime
import random

from flask import Flask
from flask import request 

import requests

import os

# Third-party libraries
from flask import Flask, redirect, request, url_for

# google libraries
# from google.oauth2 import id_token
# from google.auth.transport import requests
# import requests

# define db filename 
db_filename = "aguadatos.db"
app = Flask(__name__)

# setup config 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# initialize app
db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats 
def success_response(data, code=200):
    """
    Generalized success response function
    """
    return json.dumps(data), code

def failure_response(message, code=404):
    """
    Generalized failure response function
    """
    return json.dumps({"error": message}), code