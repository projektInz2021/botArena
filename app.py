from flask import Flask, render_template
from flask_login import login_required, current_user
from flask_cors import CORS
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

@app.route('/')
def home():
    return render_template("index.html",message="Work in progress...")

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
    app.run()