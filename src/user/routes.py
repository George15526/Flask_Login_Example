from . import user_bp
from flask import render_template, redirect, url_for, flash, request
from src import db
from src.models import User
from flask_login import login_user, logout_user, login_required

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        print(username, password, confirm_password)
        
        user_exist = User.query.filter_by(email=email).first()
        if user_exist:
            flash('Email already exists')
              
        else:
            if password != confirm_password:
                flash('Passwords do not match')
            else:
                new_user = User(username=username, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                flash('User created, please login', 'success')
                return redirect(url_for('user_bp.login'))
        
    return render_template('register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            if user.password == password:
                login_user(user)
                print("Login success")
                return redirect(url_for('user_bp.dashboard'))
            else:
                print("Login failed")
                flash('Incorrect password', 'danger')
        # return redirect(url_for('user_bp.login'))
    return render_template('login.html')

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return '''
    <h1>Welcome friend, this is dashboard</h1>
    <a href="/user/logout">Logout</a>
    '''

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    print('User logout')
    return redirect(url_for('user_bp.login'))
