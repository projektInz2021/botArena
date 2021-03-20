from flask import Blueprint, render_template, redirect, url_for
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    #login page code here
    pass

@auth.route('/register')
def register():
    #register page code here
    pass