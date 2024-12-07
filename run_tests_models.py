
import unittest
import sys
import coverage
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

cov = coverage.Coverage()
cov.start()


def run_tests_models():
   
        tests = unittest.TestLoader().discover('tests/models', pattern='test_*.py')
        unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    run_tests_models()

    cov.stop()
    cov.save()

    cov.html_report(directory='covhtml')
