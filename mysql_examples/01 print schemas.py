import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>'
)

cursor = db.cursor()
cursor.execute('SHOW DATABASES')

print('\n###############\n## DATABASES ##\n###############\n')
for database in cursor:
    print(database[0])
