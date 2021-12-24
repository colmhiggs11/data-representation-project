import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MaeveD29",
    database = "colmtesting"
)

cursor = db.cursor()
sql = "Select * from product1"

values = ( 1, )
cursor.execute(sql)

result = cursor.fetchall()
for x in result:
    print(x)
