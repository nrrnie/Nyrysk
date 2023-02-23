from flask import Blueprint
from pymongo import MongoClient

accounts = Blueprint('accounts', __name__, template_folder='templates', static_folder='static')

client = MongoClient('mongodb://localhost:27017/')
db = client['project']

from project.accounts import routes