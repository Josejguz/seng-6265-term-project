import unittest
from models.budget import Budget

class TestAddExpense(unittest.TestCase):

    def setUp(self):
        self.budget = Budget("test_budget")

    def testAddExpense(self):
        self.budget.add_expense('Utilities', 150)
        self.assertEqual(self.budget.expenses, [{'category': 'Utilities', 'amount': 150}])

    def testAddExpenseZero(self):
        self.budget.add_expense('Food', 0)
        self.assertEqual(self.budget.expenses, [])

    def testAddExpenseZero(self):
        self.budget.add_expense('Gas', -50)
        self.assertEqual(self.budget.expenses, [])
            
if __name__ == '__main__':
    unittest.main() 
