import unittest
from seng_6265_term_project.models.budget import Budget

class TestAddIncome(unittest.TestCase):

    def setUp(self):
        self.budget = Budget("test_budget")

    def test_add_income(self):
        self.budget.add_income('Job', 1000)
        self.assertEqual(self.budget.incomes, [{'source': 'Job', 'amount': 1000}])

    def test_add_income_zero_amount(self):
        self.budget.add_income('Job', 0)
        self.assertEqual(self.budget.incomes, [])

    def test_add_income_negative_amount(self):
        self.budget.add_income("Gift", -500)
        self.assertEqual(self.budget.incomes, [])

    def test_add_multiple_incomes(self):
        self.budget.add_income('Job', 1000)
        self.budget.add_income('Freelance', 500)
        self.assertEqual(self.budget.incomes, [{'source': 'Job', 'amount': 1000}, {'source': 'Freelance', 'amount': 500}])

    def test_add_income_larget_amount(self):
        self.budget.add_income('Investment', 1_000_000_000)
        self.assertEqual(self.budget.incomes, [{'source': 'Investment', 'amount': 1_000_000_000}])

    def test_add_income_float_amount(self):
        self.budget.add_income('Tips', 0.01)
        self.assertEqual(self.budget.incomes, [{'source': 'Tips', 'amount': 0.01}])

    def test_add_income_empty_amount(self):
        with self.assertRaises(ValueError):
            self.budget.add_income('Job', '')

    def test_add_income_empty_source(self):
        with self.assertRaises(ValueError):
            self.budget.add_income('', 200)

    def test_add_income_empty_amount(self):
        with self.assertRaises(ValueError):
            self.budget.add_income('Job', None)

    def test_add_income_string_amount(self):
        with self.assertRaises(TypeError):
            self.budget.add_income('Job', 'Pancakes')
            
if __name__ == '__main__':
    unittest.main() 