from flask import Flask, render_template

server = Flask(__name__)

@server.route('/')
def index():
    return 'Hello Flask app'

@server.route('/dashboard')
def dashboard():
    return render_template('dashboard.iframe.html', title='Dashboard')