from flask import Blueprint, redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required
from passlib.hash import sha256_crypt
import models

authorize = Blueprint('authorize', __name__,template_folder='templates')

from app import db

@authorize.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = models.User.query.filter_by(email=email).first()

        if not user or not sha256_crypt.verify(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('authorize.login'))
        
        login_user(user, remember=remember)

        return redirect(url_for('app.profile/{user.name}'))

@authorize.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = models.User.query.filter_by(email=email).first()

    if user:
        return redirect(url_for('authorize.register'))

    new_user = models.User(email=email, name=name, password=sha256_crypt.encrypt(password))

    db.session.add(new_user)
    db.session.commit()

    if user:
        flash('Email address already exists')
        return redirect(url_for('authorize.register'))

    return redirect(url_for('authorize.login'))

@authorize.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.index'))