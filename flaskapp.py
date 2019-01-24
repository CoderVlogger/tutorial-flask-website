from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/hello')
def hello():
    return 'Hello, World'
