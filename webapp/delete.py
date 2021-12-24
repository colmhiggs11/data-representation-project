import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MaeveD29",
    database = "colmtesting"
)

cursor = db.cursor()
sql = "delete from Product1 where pr_cleanroom =  %s"

values = (3,)
cursor.execute(sql, values)

db.commit()
print("delete complete")
