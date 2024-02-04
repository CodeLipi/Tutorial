import mysql.connector as mys

# connect the server
con = mys.connect(
    host = 'localhost',
    user = 'root',
    password = 'kushrohit',
    database = 'testdb'
)

cur = con.cursor()

# creating table
# cur.execute('CREATE TABLE customers (name VARCHAR(255), city VARCHAR(255))')

# cur.execute('SHOW TABLES')
# for tb in cur:
#     print(tb) # if not exist shows an error

# insert a records
# sql = 'INSERT INTO customers (name, city) VALUES (%s, %s)'
# val = ('Jenny', 'Ohio')
# cur.execute(sql,val)
# con.commit()
# print(cur.rowcount,'record inserted')


# insert multiple records
# sql = 'INSERT INTO customers (name, city) VALUES (%s, %s)'
# val = [
#     ('Jenny', 'Ohio'),
#     ('Peter', 'Lowstreet'),
#     ('Amy', 'Street 47'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# cur.executemany(sql,val)
# con.commit()
# print(cur.rowcount,'record inserted')

# return insert id
sql = 'INSERT INTO customers (name, city) VALUES (%s, %s)'
val = ('kush', 'Mumbai')
cur.execute(sql,val)
con.commit()
print(cur.rowcount,'record inserted',cur.lastrowid)