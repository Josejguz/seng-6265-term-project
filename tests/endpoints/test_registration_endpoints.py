import unittest
from seng_6265_term_project import create_app

class TestRegistrationEndpoints(unittest.TestCase):

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
            
            self.db = self.db.client['budget_app_test']


    def test_registration_authenticated(self):

        response = self.client.post('/auth/register', data=dict(username='test_user1', password='testpass'))
        self.assertEqual(response.status_code, 302)
        
    def test_registration_duplicate(self):
        self.client.post('/auth/register', data=dict(username='test_user', password='testpass'))
        duplicate_response = self.client.post('/auth/register', data=dict(username='test_user', password='testpass'))
        self.assertEqual(duplicate_response.status_code, 400)
        self.assertIn(b'User already exists', duplicate_response.data)

    def tearDown(self):
        with self.app.app_context():
            self.db.users.delete_one({'username': 'test_user'})
            self.db.client.drop_database('budget_app_test')
            self.db.client.close()

if __name__ == '__main__':
    unittest.main()