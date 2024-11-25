from flask import Blueprint, request, render_template, redirect, url_for, session, current_app
from models.user import User
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

auth_bp = Blueprint('auth', __name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client.budget_app

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        user = User(username, password)
        db = current_app.db
        if user.save_user(db):
            return redirect(url_for('auth.login'))
        return "User already exists", 400
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        user = User(username, password)
        db = current_app.db
        if user.verify_user(db):
            session['username'] = username
            return redirect(url_for('budget.dashboard'))
        return "Invalid credentials", 401
    return render_template('login.html')
