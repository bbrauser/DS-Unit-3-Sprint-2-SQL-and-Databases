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


# Closing cursor
pg_curs.close()


# Connecting for titanic
sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()


# Retrieving titanic
get_passengers= "SELECT * FROM titanic;"
sl_curs.execute(get_passengers)
passengers = sl_curs.fetchall()
sl_curs.execute('PRAGMA table_info(titanic);')
sl_curs.fetchall()


# Creating character table
create_titanic_passengers_table = """
CREATE TABLE titanic_passengers (
    Survived INT, 
    Pclass INT, 
    Name TEXT, 
    Sex TEXT,
    Age INT, 
    Siblings_Spouses_Aboard INT, 
    Parents_Children_Aboard INT, 
    Fare INT
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
pg_curs.execute(create_titanic_passengers_table)
pg_conn.commit()


# Inserting characters into empty table
for passenger in passengers:
  insert_passenger = """
    INSERT INTO titanic_passengers
    (Survived, Pclass, Name, Sex, Age, Siblings/Spouses_Aboard, Parents/Children_Aboard, Fare)
    VALUES """ + str(passenger[1:]) + ";"
  pg_curs.execute(insert_passenger)


# Commiting to database
pg_conn.commit()
pg_curs.execute('SELECT * FROM titanic_passengers;')
pg_passengers = pg_curs.fetchall()
for passenger, pg_passenger in zip(passengers, pg_passengers):
  assert passenger == pg_passenger


# Closing connection
pg_curs.close()
pg_conn.close()
sl_curs.close()
sl_conn.close()