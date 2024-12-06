import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from seng_6265_term_project import create_app
import os

config_name = os.getenv('FLASK_CONFIG', 'default')
app, db = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)