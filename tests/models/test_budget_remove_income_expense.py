import unittest
from seng_6265_term_project.models.budget import Budget

class TestRemoveIncomeExpense(unittest.TestCase):

    def setUp(self):

        self.budget = Budget("test_budget")
        self.budget.incomes = [
            {'source': 'Job', 'amount': 1000}, 
            {'source': 'Freelance', 'amount': 500},
            {'source': 'Side Hustle', 'amount': 200}
        ]
        self.budget.expenses = [
            {'category': 'Utilities', 'amount': 200}, 
            {'category': 'Rent', 'amount': 700},
            {'category': 'Entertainment', 'amount': 100}
        ]

    def test_remove_single_income(self):
        self.budget.remove_income('Job', 1000)
        self.assertEqual(self.budget.incomes, [
            {'source': 'Freelance', 'amount': 500},
            {'source': 'Side Hustle', 'amount': 200}
        ])

    def test_remove_multiple_incomes(self):
        self.budget.remove_income('Job', 1000)
        self.budget.remove_income('Freelance', 500)
        self.assertEqual(self.budget.incomes, [
            {'source': 'Side Hustle', 'amount': 200}
        ])

    def test_remove_single_expense(self):
        self.budget.remove_expense('Rent', 700)
        self.assertEqual(self.budget.expenses, [
            {'category': 'Utilities', 'amount': 200}, 
            {'category': 'Entertainment', 'amount': 100}
        ])

    def test_remove_multiple_expenses(self):
        self.budget.remove_expense('Rent', 700)
        self.budget.remove_expense('Utilities', 200)
        self.assertEqual(self.budget.expenses, [{'category': 'Entertainment', 'amount': 100}])

    def test_remove_incomes_and_expenses(self):
        self.budget.remove_income('Job', 1000)
        self.budget.remove_expense('Rent', 700)
        self.assertEqual(self.budget.incomes, [
            {'source': 'Freelance', 'amount': 500},
            {'source': 'Side Hustle', 'amount': 200}
        ])
        self.assertEqual(self.budget.expenses, [
            {'category': 'Utilities', 'amount': 200},
            {'category': 'Entertainment', 'amount': 100}
        ])

if __name__ == '__main__':
    unittest.main()
