from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/beer')
def beer():
    return 'Beer is Good!'

app.run()