from flask import Flask, request, make_response, redirect, url_for, abort, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<int:id>')
def user_by_id(id):
    return f'<h1>User Id is :{id}</h1>'

@app.route('/error')
def error():
    return '<h1>Bad request</h1>', 400

if __name__ == '__main__':
    manager.run()