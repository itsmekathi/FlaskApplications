from flask import Flask
from flask_sqlalchemy import SQLAlchemy, get_debug_queries


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debugsqlalchemy.db'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner') 
    # When using relationship use the model name

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id')) 
    # When using ForeignKey use the table name
    

@app.route('/')
def index():
    a = User.query.filter_by(name='Kathiravan').first()
    return "Hello "+ a.name

def sql_debug(response):
    queries = list(get_debug_queries())
    query_str = ''
    total_duration = 0.0
    for q in queries:
        total_duration += q.duration
        stmt = str(q.statement % q.parameters).replace('\n', '\n       ')
        query_str += f'Query: {stmt}\nDuration: {round(q.duration * 1000, 2)}ms\n\n'
    print('=' * 80)
    print(f'SQL Queries - {len(queries)} Queries Executed in {round(total_duration * 1000, 2)}ms')
    print('=' * 80)
    print(query_str.rstrip('\n'))
    print('=' * 80 + '\n')

    return response
app.after_request(sql_debug)

if __name__ == '__main__':
    app.run(debug=True)
