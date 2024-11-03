from seng_6265_term_project import create_app

app, db = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)