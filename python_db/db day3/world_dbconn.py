import pymysql

def mysql_world_conn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='world',
        port=3306
    )
    return conn