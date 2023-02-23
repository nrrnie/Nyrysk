from flask import Blueprint
from pymongo import MongoClient

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')
client = MongoClient('mongodb://localhost:27017/')
db = client['project']


from project.users import routes