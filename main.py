from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

@app.route('/dashboard')
def dashboard():
    return '<h1>This is a Dashboard!</h1>'

app.run(debug=True)