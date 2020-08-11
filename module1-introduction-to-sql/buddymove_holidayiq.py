import sqlite3
import pandas as pd


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()


# curs.execute('CREATE TABLE review (User_Id, Sports, Religious, Nature, Theatre, Shopping, Picnic)')
# conn.commit()


df = pd.read_csv('/Users/bradbrauser/unit3/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
df.to_sql('review', conn, if_exists='replace', index = False)


rows = 'SELECT COUNT(*) FROM review;'
curs.execute(rows)
row_result = curs.fetchall()
print('Number of rows:', row_result[0][0])


nature_shopping = """
    SELECT User_Id, Nature, Shopping 
    FROM review
    WHERE Nature >= 100
    AND Shopping >= 100
"""
curs.execute(nature_shopping)
ns_result = curs.fetchall()
print('Number of rows:', ns_result)