import sqlite3


def connect_to_db(db_name='titanic.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_TITANIC = """
    SELECT *
    FROM titanic;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    

"""
How many passengers survived?
"""
survivors = 'SELECT COUNT(*) FROM titanic WHERE Survived = 1;'
tot_survivors = execute_query(curs, survivors)
print('Number of survivors:', tot_survivors[0][0])


"""
How many passengers died?
"""
victims = 'SELECT COUNT(*) FROM titanic WHERE Survived = 0;'
tot_victims = execute_query(curs, victims)
print('Number of survivors:', tot_victims[0][0])


"""
How many passengers were in each class?
"""
pass_class_surv = """
SELECT COUNT(Pclass)
FROM Titanic
WHERE Survived = 1
GROUP BY Pclass
ORDER BY Pclass DESC;
"""
pass_class_vic = """
SELECT COUNT(Pclass)
FROM Titanic
WHERE Survived = 0
GROUP BY Pclass
ORDER BY Pclass DESC; 
"""


class_surv = execute_query(curs, pass_class_surv)
class_vic = execute_query(curs, pass_class_vic)
print ('Survivors in class 3:', class_surv[0][0])
print ('Survivors in class 2:', class_surv[1][0])
print ('Survivors in class 1:', class_surv[2][0])
print ('Victims in class 3:', class_vic[0][0])
print ('Victims in class 2:', class_vic[1][0])
print ('Victims in class 1:', class_surv[2][0])


"""
What was the average age of survivors vs nonsurvivors?
"""
surv_age = """
SELECT ROUND(AVG(Age), 0)
FROM titanic
WHERE Survived = 1;
"""
vic_age = """
SELECT ROUND(AVG(Age), 0)
FROM titanic
WHERE Survived = 0;
"""
avg_surv_age = execute_query(curs, surv_age)
avg_vic_age = execute_query(curs, vic_age)
print ('Average age of survivors:', avg_surv_age[0][0])
print ('Average age of victims:', avg_vic_age[0][0])


"""
What was the average age of each passenger class?
"""
avg_age_class = """
SELECT ROUND(AVG(Age), 0)
FROM titanic
GROUP BY Pclass
ORDER BY Pclass DESC;
"""
class_avg_age = execute_query(curs, avg_age_class)
print ('Average age of passenger in class 3:', class_avg_age[0][0])
print ('Average age of passenger in class 2:', class_avg_age[1][0])
print ('Average age of passenger in class 1:', class_avg_age[2][0])


"""
What was the average fare by passenger class?
"""
avg_fare_class = """
SELECT ROUND(AVG(Fare), 2)
FROM titanic
GROUP BY Pclass
ORDER BY Pclass DESC;
"""
class_avg_fare = execute_query(curs, avg_fare_class)
print ('Average fare of passenger in class 3:', class_avg_fare[0][0])
print ('Average fare of passenger in class 2:', class_avg_fare[1][0])
print ('Average fare of passenger in class 1:', class_avg_fare[2][0])


"""
What was the average fare by survival?
"""
avg_fare_surv = """
SELECT ROUND(AVG(Fare), 2)
FROM titanic
GROUP BY Survived
ORDER BY Survived DESC; 
"""
surv_avg_fare = execute_query(curs, avg_fare_class)
print ('Average fare of surviving passengers:', surv_avg_fare[0][0])
print ('Average fare of victim passengers:', surv_avg_fare[1][0])


"""
How many siblings/spouses aboard on average, by passenger class? By survival?
"""
avg_ss = """
SELECT ROUND(AVG(Siblings/Spouses_Aboard), 2)
FROM titanic
"""
surv_avg_ss = execute_query(curs, avg_ss)
print ('Average number of siblings/spouses aboard:', surv_avg_ss[0][0])