from flask import redirect, url_for, Blueprint, request, session
from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['project']


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    

    from project.items import items
    app.register_blueprint(items, url_prefix='/items')
    from project.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from project.accounts import accounts
    app.register_blueprint(accounts, url_prefix='/accounts')
    from project.vendors import vendors
    app.register_blueprint(vendors, url_prefix='/vendors')
    from project.users import users
    app.register_blueprint(users, url_prefix='/users')


    @app.route('/')
    def index():
        if not session.get('name'):
                return redirect(url_for('auth.login'))
        return render_template("index.html")
    
    @app.route('/tech')
    def tech():
         return render_template('tech.html')

    return app


