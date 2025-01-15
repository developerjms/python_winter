import pymysql

def mysql_book_conn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bookdb',
        port=3306
    )
    return conn