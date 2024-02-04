# 2nd way to connect

from mysql.connector import connection

con = connection.MySQLConnection(
    user = 'root',
    host = 'localhost',
    password = 'kushrohit'
)

print(con)
con.close()