# Create Read Update Delete
# CRUD
# PEP 8
# PEP 249 (connection, cursor)

import sqlite3
# Connection
connection = sqlite3.connect('films_db.sqlite')

# cursor
cursor = connection.cursor()

"""result = cursor.execute( """
#insert into genres (id, title)
#values(12,'Жанр12')
"""
).fetchall()"""

result = cursor.execute( """
Update films 
 set duration = 282 where title = 'Аватар'
"""
).fetchall()
chioce = input('хрен тебе: Y')
if chioce == 'Y':
    connection.commit()

#elements = result.fetchall()
#elements = result.fetchone()
#elements = result
for item in result:
    print(item)

connection.close()

