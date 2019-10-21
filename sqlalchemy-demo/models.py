from app import db
from datetime import datetime


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # One user linked to multiple addresses,
    # property person can be used on address entity to get the person details
    addresses = db.relationship('Address', backref='person', lazy=True)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return '<Person %r>' % self.name


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), nullable=False)

    def __repr__(self):
        return '<Address %r>' % self.email


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)
    category = db.relationship(
        'Category', backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


