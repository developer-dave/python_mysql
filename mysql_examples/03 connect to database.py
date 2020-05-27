import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>',
    database='my_database'
)

cursor = db.cursor()
cursor.execute('SHOW TABLES')

print('\n############\n## TABLES ##\n############\n')
for table in cursor:
    print(table[0])
