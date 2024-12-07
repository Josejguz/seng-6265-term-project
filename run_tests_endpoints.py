
import unittest
from seng_6265_term_project import create_app
import sys
import coverage
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

cov = coverage.Coverage()
cov.start()

def run_tests():
    # Create a Flask app with the testing configuration
    app, db = create_app('testing')
    

    # Use the app context for your tests
    with app.app_context():
        # Discover and run tests
        tests = unittest.TestLoader().discover('tests/endpoints', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    run_tests()

    cov.stop()
    cov.save()

    cov.html_report(directory='covhtml')