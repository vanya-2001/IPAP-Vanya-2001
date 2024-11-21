# pip install psycopg2

import  psycopg2
connection = psycopg2.connect(user='postgres', password="Ikzggf098", host='127.0.0.1', port='5432', database='Lib')
print(connection)
cursor = connection.cursor()

result = cursor.execute("""select * from reader""")

result_set = cursor.fetchall()
for record in result_set:
    print("Результат", record)

connection.close()
