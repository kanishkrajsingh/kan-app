import mysql.connector

dataBase =mysql.connector.connect(

    host = 'localhost',
    user='root',
    passwd = 'Root123!',

)
CursorObject = dataBase.cursor()

CursorObject.execute("CREATE DATABASE kanchan ")
print("all done")
