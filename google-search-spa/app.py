# app.py

from flask import Flask, request, jsonify, make_response
from dbsetup import createconnection, selectallitems, insertdb, createtable
import json

app = Flask(__name)
database = "./pythonsqlite.db"

# create a database connection
conn = create_connection(database)

# create items table
create_table(conn)

c = conn.cursor()

def main():
    global c

@app.route('/search', methods=_[_'GET'])
def search():
    data = request.args.get("name")
    output = select_all_items(c, data)
    return json.dumps(output)

@app.route('/insert', methods=_[_'POST'])
def insert():
    content = request.json
    name = content_[_'name']
    body = content_[_'body']
    insert_db(c, name, body)
    return "Successful"

if _**name == '**_main_':
    main()
    app.run(debug=True)