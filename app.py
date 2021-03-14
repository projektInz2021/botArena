from flask import Flask
import os
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    #home page code here
    pass

@app.route('/login')
def login():
    #login page code here
    pass

@app.route('/register')
def register():
    #register page code here
    pass

if __name__ == '__main__':
    app.run()