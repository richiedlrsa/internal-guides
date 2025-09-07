from flask import Blueprint, render_template, flash, redirect, url_for
from .models import User
from .forms import RegisterUser, LoginUser
from . import db, bcrypt
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterUser()
    
    if form.validate_on_submit():
        
        if User.query.filter_by(email = form.email.data).first():
            form.email.errors.append('Email already exists')
        else:
            pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data, password = pw_hash)
            db.session.add(user)
            db.session.commit()
        
            flash('Account created successfully!', category = 'success')
        
            return redirect(url_for('views.home'))
    
    return render_template('register.html', form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginUser()
    
    if form.validate_on_submit():
        
        user = User.query.filter_by(email = form.email.data).first()
        
        if not user:
            form.email.errors.append('This email does not exist')
        elif not bcrypt.check_password_hash(user.password, form.password.data):
            form.password.errors.append('Invalid password')
        else:
            login_user(user)
            flash('Logged in successfully!', category = 'success')
            
            return redirect(url_for('views.home'))
    
    return render_template('login.html', form = form)


