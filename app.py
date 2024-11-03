from seng-6265-term-project import create_app

app, db = create_app('development')

if __name__ == '__main__':
    app.run(debug=True)