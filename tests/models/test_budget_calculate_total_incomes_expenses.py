import unittest
from seng_6265_term_project.models.budget import Budget

class TestCalculateTotalIncomesExpenses(unittest.TestCase):

    def setUp(self):
        self.budget = Budget("test_budget")

    def test_calculate_total_incomes_single(self):
        self.budget.incomes = [{'source': 'Job', 'amount': 1500}]
        self.assertEqual(self.budget.calculate_total_income(), 1500)

    def test_calculate_total_incomes_multiple(self):
        self.budget.incomes = [{'source': 'Job', 'amount': 1500}, {'source': 'Side Hustle', 'amount': 200}]
        self.assertEqual(self.budget.calculate_total_income(), 1700)

    def test_calculate_total_incomes_empty(self):
        self.budget.incomes = []
        self.assertEqual(self.budget.calculate_total_income(), 0)
    
    def test_calculate_total_expenses_single(self):
        self.budget.expenses = [{'category': 'Utilities', 'amount': 200}]
        self.assertEqual(self.budget.calculate_total_expenses(), 200)

    def test_calculate_total_expenses_multiple(self):
        self.budget.expenses = [{'category': 'Utilities', 'amount': 200}, {'category': 'Rent', 'amount': 500}]
        self.assertEqual(self.budget.calculate_total_expenses(), 700)

    def test_calculate_total_expenses_empty(self):
        self.budget.expenses = []
        self.assertEqual(self.budget.calculate_total_expenses(), 0)

if __name__ == '__main__':
    unittest.main()