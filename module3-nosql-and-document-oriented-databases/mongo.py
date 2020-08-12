import pymongo
import json
import sqlite3


# Establishing connection and cursor
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# Function to execute queries
def get_query(query):
    curs.execute(query)
    return curs.fetchall()


# Query to get character info
query = 'SELECT * FROM charactercreator_character LIMIT 20;'
results = get_query(query)


# For loop to extract info
all_character = []
for c in results:
    doc = {
        'character_id': c[0], 
        'name': c[1], 
        'level': c[2], 
        'exp': c[3], 
        'hp': c[4], 
        'strength': c[5], 
        'intelligence': c[6], 
        'dexterity': c[7], 
        'wisdom': c[8]
    }
    all_character.append(doc)


# Connection to MongoDB
client = pymongo.MongoClient("mongodb+srv://bbrauser:L7ZuCW**********@cluster0.qqq6g.gcp.mongodb.net/RPG_Characters?retryWrites=true&w=majority")
db = client.RPG_Characters


# Inserting the character info
db.RPG_Characters.insert_many(all_character)


print(*db.RPG_Characters.find())


# QUESTION: How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
# ANSWER: I think that loading info into MongoDB was much easier than in PostgreSQL because we didn't have to specify types, 
# but creating the databases in MongoDB was MUCH harder than in PostgreSQL. Overall, I do prefer to work with MongoDB because
# once the cluster is set up, the data is much easier to load.