import mysql.connector

SELECT_ALL_BOOKS = 'SELECT ID, TITLE, AUTHOR FROM BOOKS'
DELETE_BOOK_BY_ID = 'DELETE FROM BOOKS WHERE ID = {id}'

db = mysql.connector.connect(
    host='localhost',
    user='<user>',
    passwd='<password>',
    database='my_database'
)

################################
# TABLE CONTENTS BEFORE DELETE #
################################

cursor = db.cursor()
cursor.execute(SELECT_ALL_BOOKS)
print('\n###########################\n## RECORDS BEFORE DELETE ##\n###########################\n')
for book in cursor:
    print(book)

#############################
# DELETE USING STATIC QUERY #
#############################


# print('\nDELETING DUPLICATE ENTRIES .... ')

# This query deletes any duplicate entries
# sql = 'DELETE B2 FROM BOOKS B1, BOOKS B2 WHERE B1.TITLE = B2.TITLE AND B1.AUTHOR = B2.AUTHOR AND B1.ID < B2.ID'
# cursor.execute(sql)
# db.commit()


##############################
# DELETE USING DYNAMIC QUERY #
##############################

print('\nDELETING BY ID ... ')

cursor.execute(SELECT_ALL_BOOKS)
result_set = cursor.fetchall()
for book in result_set:
    book_id = book[0]
    print('Deleting row with id:', book_id)
    delete_query = DELETE_BOOK_BY_ID.format(id=book_id)
    cursor.execute(delete_query)
    db.commit()

###############################
# TABLE CONTENTS AFTER DELETE #
###############################

cursor.execute(SELECT_ALL_BOOKS)
print('\n##########################\n## RECORDS AFTER DELETE ##\n##########################\n')
for book in cursor:
    print(book)


