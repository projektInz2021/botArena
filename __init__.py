from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import authorize as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app