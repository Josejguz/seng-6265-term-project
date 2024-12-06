from flask import Blueprint, request, session, redirect, url_for, render_template, current_app
from ..models.budget import Budget
from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

budget_bp = Blueprint('budget', __name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client.budget_app

@budget_bp.route('/dashboard')
def dashboard():
    if 'username' in session:
        user_budgets = db.budgets.find({"username": session['username']})
        budgets = []
        for budget in user_budgets:
            for key, value in budget.items():
                if key != "_id" and key != "username":
                    budget = Budget(key)

                    budget.incomes = value.get('incomes', [])
                    budget.expenses = value.get('expenses', [])

                    total_income = budget.calculate_total_income()
                    total_expenses = budget.calculate_total_expenses()
                    remaining = budget.calculate_savings()
                    
                    budgets.append({
                        "name": key,
                        "total_income": total_income,
                        "total_expenses": total_expenses,
                        "remaining": remaining,
                        "incomes": budget.incomes,
                        "expenses": budget.expenses
                    })
        return render_template('dashboard.html', username=session['username'], budgets=budgets)
    return redirect(url_for('auth.login'))

@budget_bp.route('/generate_report/<budget_name>', methods=['GET']) 
def generate_report(budget_name): 
    if 'username' in session: 
        db = current_app.db
        budget = Budget.load_budget(db, session['username'], budget_name) 
        if budget: 
            report = budget.generate_report() 
            return render_template('report.html', report=report) 
        return "Budget not found", 404 
    return "Unauthorized", 401

@budget_bp.route('/create_budget', methods=['POST'])
def create_budget():
    if 'username' in session:
        data = request.form
        name = data['name']
        budget = Budget(name)
        if budget.save_budget(db, session['username']):
            print("Budget saved successfully")
            return redirect(url_for('budget.dashboard'))
        else:
            print("Failed to save budget")
        return "Failed to create budget", 400
    return "Unauthorized", 401

@budget_bp.route('/add_income', methods=['POST'])
def add_income():
    if 'username' in session:
        data = request.form
        budget_name = data['budget_name']
        income_source = data['income_source']
        income_amount = float(data['income_amount'])
        budget = Budget.load_budget(db, session['username'], budget_name)
        if budget:
            budget.add_income(income_source, income_amount)
            budget.save_budget(db, session['username'])
            return redirect(url_for('budget.dashboard'))
        return "Budget not found", 404

@budget_bp.route('/add_expense', methods=['POST'])
def add_expense():
    if 'username' in session:
        data = request.form
        budget_name = data['budget_name']
        category = data['category']
        amount = float(data['amount'])
        budget = Budget.load_budget(db, session['username'], budget_name)
        if budget:
            budget.add_expense(category, amount)
            budget.save_budget(db, session['username'])
            return redirect(url_for('budget.dashboard'))
        return "Budget not found", 404
    return "Unauthorized", 401

@budget_bp.route('/delete_income', methods=['POST'])
def delete_income():
    if 'username' in session:
        data = request.form
        budget_name = data['budget_name']
        income_source = data['income_source']
        income_amount = float(data['income_amount'])
        budget = Budget.load_budget(db, session['username'], budget_name)
        if budget:
            budget.remove_income(income_source, income_amount)
            budget.save_budget(db, session['username'])
            return redirect(url_for('budget.dashboard'))
        return "Budget not found", 404
    return "Unauthorized", 401

@budget_bp.route('/delete_expense', methods=['POST'])
def delete_expense():
    if 'username' in session:
        data = request.form
        budget_name = data['budget_name']
        expense_category = data['expense_category']
        expense_amount = float(data['expense_amount'])
        budget = Budget.load_budget(db, session['username'], budget_name)
        if budget:
            budget.remove_expense(expense_category, expense_amount)
            budget.save_budget(db, session['username'])
            return redirect(url_for('budget.dashboard'))
        return "Budget not found", 404
    return "Unauthorized", 401

@budget_bp.route('/delete_budget', methods=['POST'])
def delete_budget():
    if 'username' in session:
        budget_name = request.form['budget_name']
        db.budgets.update_one({"username": session['username']}, {"$unset": {budget_name: 1}})
        return redirect(url_for('budget.dashboard'))
    return "Unauthorized", 401