from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<foo>')
def hello(foo):
    return render_template('hello.html',balls=foo,L=range(10))

@app.route('/beer1')
def beer():
    return 'Beer is Good!'

app.run(host='0.0.0.0', debug=True)