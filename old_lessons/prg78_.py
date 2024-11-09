# Create Read Update Delete
# CRUD
# PEP 8
# PEP 249 (connection, cursor)

import sqlite3
# Connection
connection = sqlite3.connect('films_db.sqlite')

# cursor
cursor = connection.cursor()

result = cursor.execute( """select title from  films
where genre = (Select id from  genres where title =?)""", ('фантастика', )
).fetchall()
#elements = result.fetchall()
#elements = result.fetchone()
#elements = result
for item in result:
    print(item)

connection.close()

