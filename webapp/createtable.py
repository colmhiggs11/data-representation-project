import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MaeveD29",
    database = "colmtesting"
)

cursor = db.cursor()
sql = "CREATE TABLE Product1 (pr_cleanroom int NOT NULL UNIQUE, Product nvarchar(255) NULL,	CountryName varchar(255) NULL,primary key(pr_cleanroom))Engine=InnoDb;"
cursor.execute(sql)