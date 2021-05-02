from flask import Blueprint, jsonify
from ..dbsetting import connect_db
# import MySQLdb

index = Blueprint('index', __name__, url_prefix='/')

# con = MySQLdb.connect(
#     user='apiuser',
#     passwd='apipasswd',
#     host='db',
#     db='sample01',
#     charset='utf8'
# )

con = connect_db()
cursor = con.cursor()


@index.route('/')
def index1():
    cur = con.cursor()
    sql = "SELECT * FROM items"
    cur.execute(sql)
    rows = cur.fetchall()

    return jsonify(rows)
