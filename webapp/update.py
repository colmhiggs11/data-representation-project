import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MaeveD29",
    database = "colmtesting"
)

cursor = db.cursor()
sql = "update Product1 set Product = %s ,CountryName = %s where pr_cleanroom =  %s"

values = ( "Promus", "Ireland", 3 )
cursor.execute(sql, values)

db.commit()
print("update complete")
