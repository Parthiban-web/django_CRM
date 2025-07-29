import mysql.connector

dataBase = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='parthiban@619'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
