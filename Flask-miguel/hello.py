from flask import Flask, request, make_response, redirect, url_for, abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    response = make_response(f'<h1>Hello World!</h1><h2>Your user agent is:{user_agent}</h2>')
    response.set_cookie('answer','42')
    response.set_cookie('application_name','Home Management system')
    return response

@app.route('/index')
def index():
    return redirect(url_for('home'))

@app.route('/user/<name>')
def user(name):
    return f'<h1>Welcome {name},</h1>'

@app.route('/user/<int:id>')
def user_by_id(id):
    return f'<h1>User Id is :{id}</h1>'

@app.route('/error')
def error():
    return '<h1>Bad request</h1>', 400

if __name__ == '__main__':
    manager.run()
