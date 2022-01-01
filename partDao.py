import mysql.connector
import dbconfig as cfg

class partDAO:
    # Connect to the Database
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host= cfg.mysql['host'],
            user= cfg.mysql['username'],
            password= cfg.mysql['password'],
            database= cfg.mysql['database']
        )
    
    def getCursor(self): 
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    def __init__(self): 
        self.connectToDB()

    # Create function using MySQL 
    def create(self, part):
        cursor = self.getCursor()
        sql="insert into Equipment (part_ID, part_name, checkedInBy, quantity) values (%s,%s,%s,%s)"
        values = [
            part['part_ID'],
            part['part_name'],
            part['checkedInBy'],
            part['quantity']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    # Function to get all data from the table
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from Equipment ORDER BY part_ID"
        cursor.execute(sql)
        result = cursor.fetchall()
        returnArray = []
       # print(result)
        for result in result:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        cursor.close()
        return returnArray

    # Find a single item in the table
    def findByID(self, part_ID):
        cursor = self.db.cursor()
        sql="select * from Equipment where part_ID = %s"
        values = [part_ID]

        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDict(result)

    # Function to update the table
    def update(self, part):
        cursor = self.db.cursor()
        sql="update Equipment set part_name= %s, checkedInBy=%s , quantity=%s  where part_ID = %s"
        values = [
            part['part_name'],
            part['checkedInBy'],
            part['quantity'],
            part['part_ID']
        ]
        
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return part

    # Delete function
    def delete(self, part_ID):
        cursor = self.db.cursor()
        sql="delete from Equipment where part_ID = %s"
        values = [part_ID]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

        return {}

    # Converting data to dictionary for ease of use.
    def convertToDict(self, result):
        colnames = ['part_ID', 'part_name', 'checkedInBy', 'quantity']
        part = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                part[colName] = value
        return part

# Creating Class instance.
partDAO = partDAO()