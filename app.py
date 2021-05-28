from flask import Flask, render_template
from flask_login import login_required, LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import TestingConfig
import auth

app = Flask(__name__)
app.register_blueprint(auth.authorize)
CORS(app)
db = SQLAlchemy(app)
test=TestingConfig()
app.config.from_object(test)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<user_name>')
@login_required
def profile(user_name):
    return{
        "user_name" : "{user_name}"
        }
@app.route('/<user_name>/profile')
def userProfile(user_name):
    #will be added when needed
    pass

if __name__ == '__main__':
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    login_manager.login_view = 'authorize.login'
    app.run()