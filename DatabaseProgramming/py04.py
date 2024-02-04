# read/fetch data form db

import mysql.connector as mys

con = mys.connect(
    user = 'root',
    password = 'kushrohit',
    host = 'localhost',
    database = 'testdb'
)

cur = con.cursor()

# cur.execute('SELECT * FROM customers')

cur.execute('SELECT name FROM customers')

# result = cur.fetchall()
# for x in result:
#     print(x)

result1 = cur.fetchone()
print(result1)