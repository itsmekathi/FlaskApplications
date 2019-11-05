from flask import render_template
from . import main

@main.route('/')
def index():
    return 'Hello Flask app'

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.iframe.html', title='Dashboard')