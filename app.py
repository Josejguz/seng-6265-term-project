from seng_6265_term_project import create_app
import os

config_name = os.getenv('FLASK_CONFIG', 'default')
app, db = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)