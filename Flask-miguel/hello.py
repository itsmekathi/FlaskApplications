from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Welcome {name},</h1>'

@app.route('/user/<int:id>')
def user_by_id(id):
    return f'<h1>User Id is :{id}</h1>'


if __name__ == '__main__':
    app.run(debug=True)