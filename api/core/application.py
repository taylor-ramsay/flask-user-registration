from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt

application = Flask(__name__)
bcrypt = Bcrypt(application)
CORS(application)