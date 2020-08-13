"""Creating and inserting data with SQLite."""

import sqlite3conn = sqlite3.connect('example_db.sqlite3')


def insert_data(conn):
    curs - conn.cursosr()
    my_data = [
        ('Malven', 7, 10),
        ('Steven', -3, 12), 
        ('Dondre', -80, -1)
    ]
    create_statement = """
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name CHAR(20), 
            favorite_number INTEGER, 
            least_favorite_number INTEGER
        );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()


def insert_data(conn):
    my_data = my_data
    for row in my_data:
        pass
        # Exercise - write an insert statement
    curse.close()
    conn.commit()

if ___Name