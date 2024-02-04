import mysql.connector as mys

# connect the server
con = mys.connect(
    host = 'localhost',
    user = 'root',
    password = 'kushrohit'
)

# print(con)

# preparing a cursor object
cur = con.cursor()

# creating db
# cur.execute('CREATE DATABASE testdb')

# cur.execute('SHOW DATABASES')
# for db in cur:
#     print(db)

# disconnect the server
con.close()