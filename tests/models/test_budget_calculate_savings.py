import unittest
from models.budget import Budget

class TestCalculateSavings(unittest.TestCase):

    def setUp(self):
        self.budget = Budget("test_budget")

    def test_calculate_savings_normal(self):
        self.budget.incomes = [{'source': 'Job', 'amount': 1500}]
        self.budget.expenses = [{'source': 'Utilities', 'amount': 200}, {'source': 'Rent', 'amount': 500}]
        self.assertEqual(self.budget.calculate_savings(), 800)

    def test_calculate_savings_no_income(self):
        self.budget.incomes = []
        self.budget.expenses = [{'source': 'Utilities', 'amount': 200}, {'source': 'Rent', 'amount': 500}]
        self.assertEqual(self.budget.calculate_savings(), -700)

    def test_calculate_saviongs_no_expenses(self):
        self.budget.expenses = []
        self.budget.incomes = [{'source': 'Job', 'amount': 1500}]
        self.assertEqual(self.budget.calculate_savings(), 1500)

    def test_calculate_savings_empty_input(self):
        self.budget.incomes = []
        self.budget.expenses = []
        self.assertEqual(self.budget.calculate_savings(), 0)

    def test_calculate_savings_mixed_input(self):
        self.budget.incomes = [{'source': 'Job', 'amount': 1500.50}, {'source': 'Side Hustle', 'amount': 200}]
        self.budget.expenses = [{'category': 'Utilities', 'amount': 200.75}, {'category': 'Rent', 'amount': 500}]
        self.assertEqual(self.budget.calculate_savings(), 999.75)

    def test_calculate_savings_negative_input(self):
        self.budget.incomes = [{'source': 'Job', 'amount': -1500}]
        self.budget.expenses = [{'category': 'Utilities', 'amount': 200}, {'category': 'Rent', 'amount': -500}]
        self.assertEqual(self.budget.calculate_savings(), -1200)

    def test_calculate_savings_muliple_steps(self):
        self.budget.incomes = []
        self.budget.expenses = []
        self.budget.add_income('Job', 1500)
        self.budget.add_income('Side Hustle', 200)
        self.budget.add_expense('Utilities', 275)
        self.budget.add_income('Freelance', 700)
        self.budget.add_expense('Rent', 950)
        self.assertEqual(self.budget.calculate_savings(), 1175)

if __name__ == '__main__':
    unittest.main()

        