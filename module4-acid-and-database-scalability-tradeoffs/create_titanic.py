# imports
import psycopg2
import pandas as pd
from psycopg2.extras import execute_values


# reading in titanic Data
df = pd.read_csv('titanic.csv')


# renaming columns in order to have them read into elephant
df['Siblings/Spouses Aboard'].rename('siblingsspouse', axis=1)
df['Parents/Children Aboard'].rename('parentschildren', axis=1)


# getting rid of unecessary apostrophies
df['Name'] = df['Name'].str.replace("'", "")


# creds for cloud DB, password is TOP SECRET
dbname = 'cwsewxgg'
user = 'cwsewxgg'  # ElephantSQL happens to use same name for db and user
password = 'mrmUpCk3SyyGEG4kW_HczxWF-4JOL-O5'  # Sensitive! Don't share/commit
host = 'drona.db.elephantsql.com'


# connection to cloud
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()


# creating Titanic Table
create_titanic_table = """
DROP TABLE IF EXISTS Titanic;
CREATE TABLE Titanic (
    index INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex TEXT,
    Age REAL,
    siblingsspouse INT,
    parentschildren INT,
    Fare REAL
);
"""


# running table and committing table
pg_curs.execute(create_titanic_table)
pg_conn.commit()


# using the execute_values function - Would like to go over this again to enhance my understanding
execute_values(pg_curs, """
INSERT INTO Titanic
(Survived, Pclass, Name, Sex, Age, siblingsspouse, parentschildren, Fare)
VALUES %s;
""", [tuple(row) for row in df.values])


# commit
pg_conn.commit()
pg_curs.execute("""
SELECT *
FROM Titanic
LIMIT 1;
""")


# printing to validate
print(pg_curs.fetchall())