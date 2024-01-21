from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    names = ['Kamal', 'Mike', 'Tom']
    return render_template('dashboard.html', names=names, condition=False)

app.run(debug=True)