import mysql.connector
class partDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MaeveD29",
        #user="datarep",  # this is the user name on my mac
        #passwd="password" # for my mac
        database="datarepresentation"
        )
    def create(self, part):
        cursor = self.db.cursor()
        sql="insert into Equipment (part_ID, part_name, checkedInBy, quantity) values (%s,%s,%s,%s)"
        values = [
            part['part_ID'],
            part['part_name'],
            part['checkedInBy'],
            part['quantity']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from Equipment"
        cursor.execute(sql)
        result = cursor.fetchall()
        returnArray = []
       # print(result)
        for result in result:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray


    def findByID(self, part_ID):
        cursor = self.db.cursor()
        sql="select * from Equipment where part_ID = %s"
        values = [part_ID]

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

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
        return part


    def delete(self, part_ID):
        cursor = self.db.cursor()
        sql="delete from Equipment where part_ID = %s"
        values = [part_ID]
        cursor.execute(sql, values)
        self.db.commit()
        return {}


    def convertToDict(self, result):
        colnames = ['part_ID', 'part_name', 'checkedInBy', 'quantity']
        part = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                part[colName] = value
        return part


partDAO = partDAO()