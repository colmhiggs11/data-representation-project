import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MaeveD29",
    database = "colmtesting"
)

cursor = db.cursor()
sql = "INSERT into Product1 (pr_cleanroom ,Product ,CountryName ) VALUES ( %s, %s, %s)"

values = (3, "Synergy", "Malaysia" )
cursor.execute(sql, values)

db.commit()
