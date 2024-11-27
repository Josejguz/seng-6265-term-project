# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:11:45 2024

@author: apgra
"""

import unittest

# Function to be tested
def create_budget(name, amount, existing_budget_names):
    if not name or name.strip() == "":
        raise ValueError("Budget name cannot be empty.")
    if name in existing_budget_names:
        raise ValueError("Budget name already exists.")
    if amount <= 0:
        raise ValueError("Budget amount must be greater than zero.")
    return {"name": name, "amount": amount}

# Test cases
class TestCreateBudget(unittest.TestCase):
    
    def test_create_budget_success(self):
        """Test creating a budget with valid inputs."""
        existing_budgets = ["Food", "Travel"]
        name = "Entertainment"
        amount = 500
        result = create_budget(name, amount, existing_budgets)
        self.assertEqual(result, {"name": "Entertainment", "amount": 500})

    def test_create_budget_duplicate(self):
        """Test creating a budget with a duplicate name."""
        existing_budgets = ["Food", "Travel"]
        name = "Food"  # Duplicate name
        amount = 100
        with self.assertRaises(ValueError):
            create_budget(name, amount, existing_budgets)

    def test_create_budget_empty_name(self):
        """Test creating a budget with an empty name."""
        existing_budgets = ["Food", "Travel"]
        name = ""  # Empty name
        amount = 100
        with self.assertRaises(ValueError):
            create_budget(name, amount, existing_budgets)

    def test_create_budget_none_name(self):
        """Test creating a budget with a None name."""
        existing_budgets = ["Food", "Travel"]
        name = None  # None name
        amount = 100
        with self.assertRaises(ValueError):
            create_budget(name, amount, existing_budgets)

    def test_create_budget_invalid_amount(self):
        """Test creating a budget with a non-positive amount."""
        existing_budgets = ["Food", "Travel"]
        name = "Savings"
        amount = 0  # Invalid amount
        with self.assertRaises(ValueError):
            create_budget(name, amount, existing_budgets)

    def test_create_budget_whitespace_name(self):
        """Test creating a budget with a name that is whitespace only."""
        existing_budgets = ["Food", "Travel"]
        name = "   "  # Whitespace name
        amount = 100
        with self.assertRaises(ValueError):
            create_budget(name, amount, existing_budgets)


# Run the tests
if __name__ == "__main__":
    unittest.main()
