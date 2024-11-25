import unittest
from models.budget import Budget

class TestGenerateReport(unittest.TestCase):

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

    def test_generate_report_normal(self):
        self.assertEqual(self.budget.generate_report(), {
            'budget_name': 'test_budget',
            'total_income': 1700,
            'total_expenses': 1000,
            'savings': 700,
            'incomes': [
                {'source': 'Job', 'amount': 1000}, 
                {'source': 'Freelance', 'amount': 500},
                {'source': 'Side Hustle', 'amount': 200}
            ],
            'expenses': [
                {'category': 'Utilities', 'amount': 200}, 
                {'category': 'Rent', 'amount': 700},
                {'category': 'Entertainment', 'amount': 100}
            ]
        })

    def test_generate_report_no_income(self):
        self.budget.incomes = []
        self.assertEqual(self.budget.generate_report(), {
            'budget_name': 'test_budget',
            'total_income': 0,
            'total_expenses': 1000,
            'savings': -1000,
            'incomes': [],
            'expenses': [
                {'category': 'Utilities', 'amount': 200}, 
                {'category': 'Rent', 'amount': 700},
                {'category': 'Entertainment', 'amount': 100}
            ]
        })

    def test_generate_report_no_expense(self):
        self.budget.expenses = []
        self.assertEqual(self.budget.generate_report(), {
            'budget_name': 'test_budget',
            'total_income': 1700,
            'total_expenses': 0,
            'savings': 1700,
            'incomes': [
                {'source': 'Job', 'amount': 1000}, 
                {'source': 'Freelance', 'amount': 500},
                {'source': 'Side Hustle', 'amount': 200}
            ],
            'expenses': []
        })

    def test_generate_report_empty_input(self):
        self.budget.incomes = []
        self.budget.expenses = []
        self.assertEqual(self.budget.generate_report(), {
            'budget_name': 'test_budget',
            'total_income': 0,
            'total_expenses': 0,
            'savings': 0,
            'incomes': [],
            'expenses': []
        })

    def test_generate_report_mixed_input(self):
        self.budget.incomes = [{'source': 'Job', 'amount': 1500.50}, {'source': 'Side Hustle', 'amount': 200}]
        self.budget.expenses = [{'category': 'Utilities', 'amount': 200.75}, {'category': 'Rent', 'amount': 500}]
        self.assertEqual(self.budget.generate_report(), {
            'budget_name': 'test_budget',
            'total_income': 1700.50,
            'total_expenses': 700.75,
            'savings': 999.75,
            'incomes': [{'source': 'Job', 'amount': 1500.50}, {'source': 'Side Hustle', 'amount': 200}],
            'expenses': [{'category': 'Utilities', 'amount': 200.75}, {'category': 'Rent', 'amount': 500}]
        })

if __name__ == '__main__':
    unittest.main()