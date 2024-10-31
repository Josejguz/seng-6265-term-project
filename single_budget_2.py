# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:23:29 2024

@author: apgra
"""

class Budget:
    def __init__(self, name):
        
        #Initializes name of budget

        self.name = name

        # Initialize empty lists for income and expenses
        
        self.incomes = []
        self.expenses = []

    def add_income(self, source, amount):
       
        # Adds income source and amount to the income list.
      
        if amount > 0:
            self.incomes.append({'source': source, 'amount': amount})
            print(f"Income of {amount} from {source} added.")
        else:
            print("Income amount must be positive.")

    def add_expense(self, description, amount):
       
        # Adds an expense description and amount to the expenses list.
             
        if amount > 0:
            self.expenses.append({'description': description, 'amount': amount})
            print(f"Expense of {amount} for {description} added.")
        else:
            print("Expense amount must be positive.")

    def calculate_savings(self):
        
       # Calculates total savings by subtracting total expenses from total income.
               
        total_income = sum([income['amount'] for income in self.incomes])
        total_expenses = sum([expense['amount'] for expense in self.expenses])
        savings = total_income - total_expenses
        return savings
    
    def generate_report(self):

        # Generates a report with the budget name, total income, total expenses, savings, income list, and expenses list.
        report = {
            'budget_name': self.name,
            'total_income': sum([income['amount'] for income in self.incomes]),
            'total_expenses': sum([expense['amount'] for expense in self.expenses]),
            'savings': self.calculate_savings(),
            'incomes': self.incomes,
            'expenses': self.expenses
        }
        return report
    
    def save_budget(self, db, username):
        user_budget = db.budgets.find_one({"username": username})
        budget_data = {
            "name": self.name,
            "incomes": self.incomes,
            "expenses": self.expenses
        }
        if user_budget:
            db.budgets.update_one({"username": username}, {"$set": {self.name: budget_data}})
        else:
            db.budgets.insert_one({"username": username, self.name: budget_data})
        return True

    