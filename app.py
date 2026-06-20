# this is my 1st push in github actions
from flask import Flask, render_template
app = Flask(__name__)

# this is #

@app.route('/')
def hello_world():
    return render_template('index.html')
# this is my 3rd github actions

@app.route('/health')
def health():
    return 'Server is up and running'
