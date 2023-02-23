from flask import Flask, session
from flask_session import Session
from pymongo import MongoClient
from project import create_app

app = create_app()
app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app=app)
client = MongoClient('mongodb://localhost:27017/')


if __name__ == '__main__':
    app.run(debug=True)