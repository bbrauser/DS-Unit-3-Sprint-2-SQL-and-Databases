import sqlite3


def connect_to_db(db_name='titanic_regress.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    

"""
How many passengers survived?
"""
survivors = 'SELECT COUNT(*) FROM titanic_regress WHERE Survived = 1;'
tot_survivors = execute_query(curs, survivors)
print('Number of survivors:', tot_survivors)