import unittest
from seng_6265_term_project import create_app
from bs4 import BeautifulSoup

class GenerateReportTestCase(unittest.TestCase):

    # Set up the test case
    def setUp(self):

        # Initialize app for testing configuration
        self.app, self.db = create_app('testing')

        # Initialize test client
        self.client = self.app.test_client()

        #Set up testing configuration
        self.app.config['TESTING'] = True

        # Set up secret key for session management
        self.app.config['SECRET_KEY'] = 'test_secret_key'

        # Set up session management
        with self.app.app_context():
            
            # Initialize test database
            self.db = self.db.client['budget_app_test']
            self.db.users.insert_one({'username': 'test_user', 'password': 'testpass'})
            self.db.budgets.insert_one({ 
            "username": "test_user", 
            "test_budget": { "name": "test_budget", 
                            "incomes": [ 
                                {"source": "salary", "amount": 4000}, 
                                {"source": "freelance", "amount": 1500} 
                            ], 
                            "expenses": [ 
                                {"category": "Rent", "amount": 1200}, 
                                {"category": "Utilities", "amount": 300}, 
                                {"category": "Groceries", "amount": 500}, 
                                {"category": "Entertainment", "amount": 200} 
                            ] 
                        } 
                    })


    # Tear down the test case
    def tearDown(self):
        
        # Drop the test database and close it
        with self.app.app_context():
            
            self.db.client.drop_database('budget_app_test')
            self.db.client.close()


    # Test generate report route for an authenticated user and verify response status and response data
    def test_generate_report_authenticated(self):
        
        # Log in the test user 
        response = self.client.post('/auth/login', data=dict(username='test_user', password='testpass'))
        self.assertEqual(response.status_code, 302)
        
        # Get the generated report for the test budget
        response = self.client.get('/budget/generate_report/test_budget')
    
        # Verify the response status code
        self.assertEqual(response.status_code, 200)
        
        # Use BeautifulSoup to parse the response data
        soup = BeautifulSoup(response.data, 'html.parser')

        # Verify the report data
        total_income_text = soup.find('p', string = 'Total Income: $5500').get_text()
        self.assertEqual(total_income_text, "Total Income: $5500")

        total_income_text = soup.find('p', string = 'Total Expenses: $2200').get_text()
        self.assertEqual(total_income_text, "Total Expenses: $2200")

        savings_text = soup.find('p', string = 'Savings: $3300').get_text()
        self.assertEqual(savings_text, "Savings: $3300")

    # Test generate report route for an unauthenticated user and verify response status and response data
    def test_generate_report_unauthenticated(self):

        # Get the generated report for the test_budget without logging in 
        response = self.client.get('/budget/generate_report/test_budget')
        
        # Verify the response status code
        self.assertEqual(response.status_code, 401)
        
        # Verify the response data
        self.assertEqual(response.data.decode(), "Unauthorized")

    # Test generate report route for a budget that does not exist and verify response status and response data
    def test_generate_report_budget_not_found(self):
            
        # Register a test user
        self.client.post('/auth/register', data=dict(username='test_user', password='testpass'))
        
        # Log in the test user
        self.client.post('/auth/login', data=dict(username='test_user', password='testpass'))

        # Get the generated report for a non-existent budget
        response = self.client.get('/budget/generate_report/non_existent_budget')
        
        # Verify the response status code
        self.assertEqual(response.status_code, 404)
        
        # Verify the response data
        self.assertEqual(response.data.decode(), "Budget not found")


if __name__ == '__main__':
    unittest.main()