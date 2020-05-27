import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>',
    database='my_database'
)

cursor = db.cursor()

sql = 'SELECT ID, TITLE, AUTHOR FROM BOOKS'
cursor.execute(sql)

#############
# FETCH ALL #
#############

result_set = cursor.fetchall()
print('\n#############\n## RECORDS ##\n#############\n')
for row in result_set:
    print(row)
    print('ID: ', row[0])
    print('TITLE: ', row[1])
    print('AUTHOR: ', row[2])
    print('-'*50)

#############
# FETCH ONE #
#############

# result_set = cursor.fetchone()
# print('\n############\n## RECORD ##\n############\n')
# print(result_set)
# print('ID: ', result_set[0])
# print('TITLE: ', result_set[1])
# print('AUTHOR: ', result_set[2])
