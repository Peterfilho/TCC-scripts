import flask
from flask import request, jsonify
import sqlite3

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

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM users;').fetchall()

    return jsonify(all_users)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/users', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('department')
    author = query_parameters.get('role')

    query = "SELECT * FROM users WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if department:
        query += ' department=? AND'
        to_filter.append(published)
    if role:
        query += ' role=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('locale.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)



app.run()
