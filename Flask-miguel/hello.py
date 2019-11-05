from flask import Flask, request, make_response, redirect, url_for, abort, render_template, session, redirect, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

# Models section
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username






@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<user>')
def user(user):
    # comments = ["This is fantastic", "How are you doing", "What is wrong with you?", "How do you feel now"]
    return render_template('user.html', user=user)

@app.route('/user/<int:id>')
def user_by_id(id):
    return f'<h1>User Id is :{id}</h1>'

@app.route('/error')
def error():
    return '<h1>Bad request</h1>', 400

@app.route('/user/new', methods=['GET','POST'])
def new_user():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            flash('Looks like you have changed your name!')
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('home'))
    return render_template('newuser.html', form=form, name=session.get('name'), known=session.get('known', False))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
    #manager.run()