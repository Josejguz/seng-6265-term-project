# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:23:25 2024

@author: apgra
"""

import unittest
from budget import create_budget, db
from .models import Budget

class BudgetCreationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the application and database for testing
        cls.app = create_budget('testingbudget1')   
        cls.client = cls.app.test_client()
        
        # Push application context for the database
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Tear down the database after tests
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        # Called before every test to setup data
        self.valid_data = {
            "name": "Groceries",
            "amount": 300.00,
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        }
        self.invalid_data = {
            "name": "",
            "amount": -200,  # Invalid negative amount
            "start_date": "2024-01-01",
            "end_date": "2023-12-31"  # Invalid date range
        }
        
        # Check creating budget with valid input
    def test_create_budget_valid_input(self):
        response = self.client.post('/create_budget', data=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Budget created successfully", response.get_data(as_text=True))
        
        # Check that budget was added to the database
        with self.app.app_context():
            budget = Budget.query.filter_by(name="Groceries").first()
            self.assertIsNotNone(budget)
            self.assertEqual(budget.amount, 300.00)
       
        # Test creating a budget with invalid input
    def test_create_budget_invalid_input(self):
        response = self.client.post('/create_budget', data=self.invalid_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid input", response.get_data(as_text=True))
        
        # Verify no budget was added with invalid data
        with self.app.app_context():
            budget = Budget.query.filter_by(name="").first()
            self.assertIsNone(budget)
            
       # Test creating a budget with missing amount field
    def test_create_budget_missing_amount(self):
        incomplete_data = self.valid_data.copy()
        incomplete_data.pop('amount')  # Remove amount key
        response = self.client.post('/create_budget', data=incomplete_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Amount is required", response.get_data(as_text=True))

        # Test creating a budget with a future start and end date
    def test_create_budget_future_dates(self):
        future_data = self.valid_data.copy()
        future_data['start_date'] = "2025-01-01"
        future_data['end_date'] = "2025-12-31"
        
        response = self.client.post('/create_budget', data=future_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Budget created successfully", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
