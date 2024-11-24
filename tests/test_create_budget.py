# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:56:50 2024

@author: apgra
"""

import unittest
from seng_6265_term_project import create_app
from models.budget import Budget

class TestCreateBudget(unittest.TestCase):

# Test to verify valid input is allowed.
    def test_create_budget_valid_input(self):
        budget = Budget("my_budget")
        self.assertEqual(budget.name, "my_budget")
        self.assertEqual(budget.incomes, [])
        self.assertEqual(budget.expenses, [])

# Test to verify empty name is not allowed.
    def test_create_budget_empty_name(self):
        with self.assertRaises(ValueError):
            Budget("")  
            
# Test to verify None as a name raises a ValueError.
    def test_create_budget_none_name(self):
        with self.assertRaises(ValueError):
            Budget(None) 
 
# Test application prevents duplicate budget names.
    def test_create_budget_duplicate(self):
        Budget("test_budget")
        with self.assertRaises(ValueError):
            Budget("test_budget")


if __name__ == '__main__':
    unittest.main()
