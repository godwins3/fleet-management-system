from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

from pymongo import MongoClient

auth = Blueprint('auth', __name__)

bcrypt = Bcrypt()

client = MongoClient('mongodb://localhost:27017/')
db = client.fleet_management
# vehicles_collection = db.

# User Registration Route
@auth.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        existing_user = db.users.find_one({'email': email})
        if existing_user:
            flash('User already exists', category='error')
            return redirect(url_for('auth.signup'))

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user object
        new_user = {
            'username': username,
            'email': email,
            'password': hashed_password  # Store the hashed password
        }

        # Insert the new user into the users collection
        db.users.insert_one(new_user)

        flash('Registration successful! Please log in.', category='success')
        return redirect(url_for('auth.login'))  # Redirect to login after signup

    return render_template('register.html')

# User Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        # Query MongoDB for user
        user = db.users.find_one({'email': email})

        if user and bcrypt.check_password_hash(user['password'], password):
            # Assuming you're using Flask-Login for session management
            # login_user(user)
            flash('Login successful!', category='success')
            return redirect('/')  # Redirect to the dashboard after login
        else:
            flash('Login failed. Check your username and/or password.', category='error')

    return render_template('login.html')

# User Logout Route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', category='success')
    return redirect(url_for('auth.login'))

# Profile route to check if user is logged in
@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)