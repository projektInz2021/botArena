from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(40), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
