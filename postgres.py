# pip install psycopg2

import  psycopg2
connection = psycopg2.connect(user='postgres', password="Ikzggf098", host='127.0.0.1', port='5432', database='Lib')

cursor =connection.cursor()

result = cursor.execute("""select nchit from reader""")

connection.close()