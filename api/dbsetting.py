import MySQLdb


def connect_db():
    con = MySQLdb.connect(
        user='apiuser',
        passwd='apipasswd',
        host='db',
        db='sample01',
        charset='utf8'
    )
    return con
