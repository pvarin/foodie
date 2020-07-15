import os
from flask import Flask

app = Flask(__name__)

testing = False
if testing:
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object(os.environ['APP_SETTINGS'])

from .database import db
from .models import *
from .routes import *

