import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>'
)

cursor = db.cursor()
cursor.execute('CREATE DATABASE my_database')
