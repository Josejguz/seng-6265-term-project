import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, Blueprint, request, session, redirect, url_for, render_template, current_app

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self, db):
        if db.users.find_one({"username": self.username}):
            return False
        db.users.insert_one({"username": self.username, "password": self.password})
        return True

    def verify_user(self, db):
        user = db.users.find_one({"username": self.username, "password": self.password})
        return user is not None


# Flask Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        user = User(username, password)
        db = current_app.db
        if user.save_user(db):
            return redirect(url_for('auth.login'))
        return "User already exists", 400
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        user = User(username, password)
        db = current_app.db
        if user.verify_user(db):
            session['username'] = username
            return redirect("budget.dashboard")
        return "Invalid credentials", 401
    return render_template('login.html')


class AuthTestCase(unittest.TestCase):

    @patch('pymongo.MongoClient')
    def setUp(self, mock_mongo_client):
        # Create a mock database
        self.mock_db = MagicMock()
        mock_mongo_client.return_value = MagicMock()
        mock_mongo_client.return_value.__getitem__.return_value = self.mock_db

        # Set up Flask app for testing
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'secret'
        self.app.register_blueprint(auth_bp)
        self.app.db = self.mock_db  # Attach mock database to the Flask app
        self.client = self.app.test_client()

    def test_register_user(self):

        # Simulate user does not exist in the database
        self.mock_db.users.find_one.return_value = None

        # Send POST request to register endpoint
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Verify that the user was inserted into the database
        self.mock_db.users.insert_one.assert_called_once_with({'username': 'testuser', 'password': 'testpassword'})

    def test_register_existing_user(self):

        # Simulate user already exists in the database
        self.mock_db.users.find_one.return_value = {'username': 'testuser', 'password': 'testpassword'}

        # Send POST request to register endpoint
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check if the response status code is 400 (bad request)
        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        # Simulate user exists in the database
        self.mock_db.users.find_one.return_value = {'username': 'testuser', 'password': 'testpassword'}

        # Send POST request to login endpoint
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Verify that the session contains the username
        with self.client.session_transaction() as sess:
            self.assertEqual(sess['username'], 'testuser')

    def test_login_invalid_credentials(self):

        # Simulate user does not exist in the database
        self.mock_db.users.find_one.return_value = None

        # Send POST request to login endpoint
        response = self.client.post('/login', data={
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })

        # Check if the response status code is 401 (unauthorized)
        self.assertEqual(response.status_code, 401)

    def test_register_user_with_existing_username(self):

        # Simulate user with the same username already exists in the database
        self.mock_db.users.find_one.return_value = {'username': 'testuser'}

        # Send POST request to register endpoint
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpassword'
        })

        # Check if the response status code is 400 (bad request)
        self.assertEqual(response.status_code, 400)
        
        # Verify that the user was not inserted into the database
        self.mock_db.users.insert_one.assert_not_called()

    

if __name__ == '__main__':
    unittest.main()
