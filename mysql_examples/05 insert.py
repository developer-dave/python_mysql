import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>',
    database='my_database'
)

cursor = db.cursor()

sql = 'INSERT INTO BOOKS (TITLE, AUTHOR) VALUES (%s, %s)'
val = ('John', 'John')
cursor.execute(sql, val)

db.commit()

print('\n################################\n## NUMBER OF RECORDS INSERTED ##\n################################\n')
print(cursor.rowcount, 'record(s) inserted.')

cursor.execute('SELECT * FROM BOOKS')

print('\n##########################\n## RECORDS AFTER INSERT ##\n##########################\n')
for book in cursor:
    print(book)
