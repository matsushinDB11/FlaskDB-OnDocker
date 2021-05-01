import MySQLdb
from MySQLdb import connections


con = MySQLdb.connect(
        user='apiuser',
        passwd='apipasswd',
        host='db',
        db='sample01',
        charset='utf8'
    )
cur = con.cursor()


def db_items_insert():
    sql = "INSERT INTO items VALUES (%s, %s)"
    # sql1 = "INSERT INTO items VALUES (1, 'Mercedes')"
    # sql2 = "INSERT INTO items VALUES (2, 'RedBull')"

    # cur.execute(sql, (1, 'Mercedes'))
    # cur.execute(sql, (2, "Redbull"))
    data = [
        (1, 'Mercedes'),
        (2, 'RedBull'),
        (3, 'Ferrari')
    ]
    cur.executemany(sql, data)
    con.commit()


def db_items_get():

    # クエリを実行する
    sql = "SELECT * FROM items"
    cur.execute(sql)

    # 実行結果をすべて取得する
    rows = cur.fetchall()
    print(rows)

    # 一行ずつ表示する
    for row in rows:
        print(row)


if __name__ == '__main__':
    db_items_insert()
    db_items_get()
    con.close()
