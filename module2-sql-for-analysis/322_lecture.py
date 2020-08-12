import psycopg2
import sqlite3


# ElephantSQL info
dbname = 'kbgqljxh'
user = 'kbgqljxh'  # ElephantSQL happens to use same name for db and user
password = 'QHI-WkUVtOcs-pFDVaPgU60nqANxVObL'  # Sensitive! Don't share/commit
host = 'isilo.db.elephantsql.com'


# Connecting
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


# Creating test_table
# create_table_statement = """
# CREATE TABLE test_table (
#         id SERIAL PRIMARY KEY,
#         name varchar(40) NOT NULL,
#         data JSONB
# );
# """

# Commiting test-Table to ElephantSQL
# pg_curs.execute(create_table_statement)
# pg_conn.commit()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()


# Inserting statement to test_table
insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
    'Zaphod Beeblebrox',
    '{"key": "value", "key2": true}'::JSONB
)
"""
pg_curs.execute(insert_statement)
pg_conn.commit()
pg_curs.execute('SELECT * FROM test_table;')
pg_curs.fetchall()


# Closing cursor
pg_curs.close()


# Connecting for rpg_db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


# Retrieving charactercreator_character
get_characters= "SELECT * FROM charactercreator_character;"
sl_curs.execute(get_characters)
characters = sl_curs.fetchall()
sl_curs.execute('PRAGMA table_info(charactercreator_character);')
sl_curs.fetchall()


# Creating character table
create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY, 
    name VARCHAR(30), 
    level INT, 
    exp INT, 
    hp INT, 
    strength INT, 
    intelligence INT, 
    dexterity INT, 
    wisdom INT
);
"""


def refresh_connection_and_cursor(conn, curs):
    curs.close()
    conn.close()
    pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs
pg_conn, pg_curs = refresh_connection_and_cursor(pg_conn, pg_curs)


# Commiting table to instance
pg_curs.execute(create_character_table)
pg_conn.commit()


# Inserting characters into empty table
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)


# Commiting to database
pg_conn.commit()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character


# Closing connection
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()