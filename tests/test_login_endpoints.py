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

    def test_login_authenticated(self):

        self.db.users.insert_one({'username': 'test_user', 'password': 'testpass'})
        response = self.client.post('/auth/login', data=dict(username='test_user', password='testpass'))
        self.assertEqual(response.status_code, 302)
        self.db.users.delete_one({'username': 'test_user', 'password': 'testpass'})

    def test_login_unauthorized(self):

        response = self.client.post('/auth/login', data=dict(username='test_user', password='testpass'))
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Invalid credentials', response.data)

    def tearDown(self):
        with self.app.app_context():
            self.db.client.drop_database('budget_app_test')
            self.db.client.close()