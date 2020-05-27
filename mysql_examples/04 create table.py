import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>',
    database='my_database'
)

cursor = db.cursor()
cursor.execute('SHOW TABLES')

print('\n##########################\n## TABLES BEFORE INSERT ##\n##########################\n')
for table in cursor:
    print(table[0])

sql = 'CREATE TABLE IF NOT EXISTS BOOKS (ID INT AUTO_INCREMENT PRIMARY KEY, TITLE VARCHAR(255), AUTHOR VARCHAR(255))'
cursor.execute(sql)
cursor.execute('SHOW TABLES')

print('\n#########################\n## TABLES AFTER INSERT ##\n#########################\n')
for table in cursor:
    print(table[0])

