import code
from flask_sqlalchemy import SQLAlchemy

import base64
import boto3
import datetime
import io
from io import BytesIO
from mimetypes import guess_extension, guess_type
import os
from PIL import Image
import random
import re
import string

import hashlib

from sqlalchemy import ForeignKey
import bcrypt

db = SQLAlchemy()

# create tables 

# create models/dbs