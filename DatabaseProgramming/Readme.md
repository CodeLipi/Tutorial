Database
--------

- Temporary storage
    - in RAM, python objects, list, typle, dict
- Permanent storage
    - File System
    - Structure Database (MySql,MSSql,Oracle..etc)
    - DataWare House
    - Cloud

Limitation of File System
----------------------------

- Less amount of data storage
- Less Security of data
- No query language supports
- Holds duplicate data

Advantage of Database
--------------------------

- Large amount of data storage
- Query language supports
- High security
- No duplicate data due to primary key

Limitations of Database
---------------------------

- Not Huge amount of data storage
- Store only structured data not unstructred data and semi-structured data like image, video etc

Python Database Programming
--------------------------------

Python has library support for every database to connect, disconnect and works with databases.

**Standard steps for Python Database Programming**
1. import database specific module </br>
`import oracledb`

2. establish connection between python program and database </br>
`connect()` method of that module

3. to execute sql queries and hold results </br>
`cursor()` method of that module

4. to execute sql queries </br>
`execute(queries)` : to execute single query </br>
`executescript(queries)` : to execute a seperate script </br>
`executemany()` : to execute multiple/parameterized query 

5. `DDL` : create, alter and delete </br>
`DML` : insert, update and delete </br>
`DQL` : select 

6. In the case of DML query.. </br>
`commit() rollback()`

7. In the case of DQL query.. </br>
`fetchone()` : to fetch only one row </br>
`fetchall()` : to fetch all rows and returns a list of rows </br>
`fetchmany()` : to fetch first n rows 

7. close the resources
`cursor.close()` : close the cursor </br>
`con.close()` : close the connection

Driver/Connector
--------------------

It is a intermediatry to talks between python program and databases
For Oracle : `oracledb`

