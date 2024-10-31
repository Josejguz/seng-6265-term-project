from flask import Flask, request, jsonify, session
from user import User
from single_budget_2 import Budget
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', '7nWCfr63Pntd1kgOCGDLQG5E0HcpVjvjrHxEjhwslrcey')

client = MongoClient(os.getenv('MONGO_URI'))
db = client.budget_app

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User(username, password)
    if user.save_user(db):
        return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"message": "User already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User(username, password)
    if user.verify_user(db):
        session['username'] = username
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/create_budget', methods=['POST'])
def create_budget():
    if 'username' in session:
        data = request.get_json()
        name = data['name']
        amount = data['amount']
        budget = Budget(name, session['username'])
        if budget.save_budget(db):
            return jsonify({"message": "Budget created successfully"}), 201
        return jsonify({"message": "Failed to create budget"}), 400
    return jsonify({"message": "Unauthorized"}), 401

@app.route('/get_budget', methods=['GET'])
def get_budget():
    if 'username' in session:
        user = User(session['username'], "")
        budget_name = request.args.get('name')
        budget_data = Budget.load_budget(db, user.username, budget_name)
        if budget_data:
            return jsonify(budget_data.generate_report()), 200
        return jsonify({"message": "No budget found"}), 404
    return jsonify({"message": "Unauthorized"}), 401

if __name__ == '__main__':
    app.run(debug=True)