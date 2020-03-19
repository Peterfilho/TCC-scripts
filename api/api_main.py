import flask
from flask import request, jsonify
import numpy as np
import sqlite3
from json import dumps
import requests
import json
import localize

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Were i am</h1>
<p>A prototype API to localize users using ieee 802.11.</p>

<p> Developed by: Peterson Medeiros</p>'''
#SQL COMMANDS - TEST ROTE
@app.route('/api/test', methods=['GET'])
def test():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
#    all_users = cur.execute('SELECT *, users.* from positions join users using(user_id) WHERE user_id=1;').fetchall()
    all_users = cur.execute('SELECT *, users.* from positions join users using(user_id);').fetchall()
    return jsonify({'TEST Result': all_users})

#TODO INSERT A IMAGE OFF MAP WERE IS
@app.route('/api/v1/resources/map', methods=['GET'])
def map():
    url = "https://drive.google.com/open?id=1Nf7s7I3iWIKLeMhF5iRjG9u7dQpOLtD8"
    result = requests.get(url).json()
    return (result)

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM users;').fetchall()

    return jsonify({'users': all_users})

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/users', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    department = query_parameters.get('department')
    role = query_parameters.get('role')

    query = "SELECT * FROM users WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if department:
        query += ' department=? AND'
        to_filter.append(department)
    if role:
        query += ' role=? AND'
        to_filter.append(role)
    if not (id or department or role):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/resources/users', methods=['POST'])
def post():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = request.get_json()
    for user in users:
        name = user['name']
        department = user['department']
        role = user['role']
        cur.execute("insert into users values(NULL, '{}','{}','{}')".format(name, department, role))
        conn.commit()
    return {'status':'success'}

@app.route('/api/v1/resources/positions/all', methods=['GET'])
def locales_all():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM positions;').fetchall()

    return jsonify({'users': all_users})

@app.route('/api/v1/resources/positions', methods=['GET'])
def locales():
    query_parameters = request.args
#PARAMETERS ON URL
    id = query_parameters.get('id')
    name = query_parameters.get('name')
    date = query_parameters.get('date')
    locale = query_parameters.get('locale')
    role = query_parameters.get('role')

    query = "SELECT *, users.* FROM positions join users using (user_id) WHERE"
    to_filter = []

    if id:
        query += ' user_id=? AND'
        to_filter.append(id)
    if date:
        query += ' date=? AND'
        to_filter.append(date)
    if locale:
        query += ' locale=? AND'
        to_filter.append(locale)
    if role:
        query += ' users.role=? AND'
        to_filter.append(role)
    if name:
        query += ' users.name=? AND'
        to_filter.append(name)

    if not (id or date or locale or role or name):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/resources/positions', methods=['POST'])
def positions_post():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = request.get_json()
    for user in users:
        user_id = user['user_id']
        search = user['search']
        result = user['result']
        locale = user['locale']
        date = user['date']
        cur.execute("insert into positions values(NULL, '{}','{}','{}','{}','{}')".format(user_id, search, result, locale, date))
        conn.commit()
    return {'status':'success'}

@app.route('/api/v1/resources/positions/app', methods=['POST'])
def positions_post_app():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    users = request.get_json()
    for user in users:
        user_id = user['user_id']
        find = user['search']
        date = user['date']

        #Exemplo
        print("valor que chega!")
        print(find)
        aux = localize.test()
        print(aux)
        aux = localize.localize(-100,-70,-68,-55,-53,-55)
        print(aux)

#        cur.execute("insert into positions values(NULL, '{}','{}', {}, {}, '{}')".format(user_id, search, resultado, local, date))
#        conn.commit()
    return {'Local': aux}

app.run()
