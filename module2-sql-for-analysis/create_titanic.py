import psycopg2
import sqlite3
import pandas as pd


conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()


curs.execute('CREATE TABLE titanic (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)')
conn.commit()


df = pd.read_csv('/Users/bradbrauser/unit3/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv')
df.to_sql('titanic', conn, if_exists='replace', index = False)