from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytomany.db'

db = SQLAlchemy(app)

subs = db.Table('subs',
                db.Column('user_id', db.Integer, db.ForeignKey(
                    'user.user_id'), primary_key=True),
                db.Column('channel_id', db.Integer, db.ForeignKey(
                    'channel.channel_id'), primary_key=True)
                )


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    channels = db.relationship(
        'Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(20), nullable=False)
    

