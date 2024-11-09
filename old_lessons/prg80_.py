# Create Read Update Delete
# CRUD
# PEP 8
# PEP 249 (connection, cursor)

import sqlite3

class DbRead:
    def __init__(self, db_name):
        if db_name =='':
            print( 'XZ')
            return
        try:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self. connection.cursor()
            print('Соединились с базой')
        except sqlite3.Error as e:
            print(f'Error : {e}')

    def read_all(self, query):
        """
        :param query:
        :return:
        """
        return self.cursor.execute(query).fetchall()

    def __del__(self):
        self.connection.close()

class dbWrite(DbRead):

db = DbRead('films_db.sqlite')
sql = '''
select * from films where year =2010
'''
result = db.read_all(sql)
#for