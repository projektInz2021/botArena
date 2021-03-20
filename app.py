from flask import Flask, render_template
from flask_login import login_required, current_user
import os
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("index.html",message="Work in progress...")

@app.route('/profile')
@login_required
def profile():
    pass

if __name__ == '__main__':
    app.run()