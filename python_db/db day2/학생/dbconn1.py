# import mysql.connector
# # python -m pip install mysql-connector-python

# DB_CONFIG = {
#     'host' : 'localhost',
#     'user' : 'root',
#     'password' : '1234',
#     'database' : 'world',
#     'port' : 3306
# }

# def get_connection():
#     return mysql.connector.connect(**DB_CONFIG)

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


