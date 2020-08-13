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
query = 'SELECT * FROM armory_weapon;'
results = get_query(query)


# For loop to extract info
all_character = []
for c in results:
    doc = {
        'item_ptr_id': c[0], 
        'power': c[1], 
        # 'value': c[2],
        # 'weight': c[3]
    }
    all_character.append(doc)


# Connection to MongoDB
client = pymongo.MongoClient("mongodb+srv://bbrauser:L7ZuCWSE0micg6Jp@cluster0.qqq6g.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.RPG_Characters


# # Inserting the character info
db.RPG_Weapons.insert_many(all_character)


# QUESTION: How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
# ANSWER: I think that loading info into MongoDB was much easier than in PostgreSQL because we didn't have to specify types, 
# but creating the databases in MongoDB was MUCH harder than in PostgreSQL. Overall, I do prefer to work with MongoDB because
# once the cluster is set up, the data is much easier to load.


"""
How many total characters are there?
"""
total = db.RPG_Characters.count_documents({})
print("Total number of characters:", total)


"""
How many clerics are there?
"""
clerics = db.RPG_Clerics.count_documents({})
print("Total number of clerics:", clerics)


"""
How many fighers are there?
"""
fighters = db.RPG_Fighters.count_documents({})
print("Total number of fighters:", fighters)


"""
How many mages are there?
"""
mages = db.RPG_Mages.count_documents({})
print("Total number of mages:", mages)


"""
How many necromancers are there?
"""
necromancers = db.RPG_Necromancers.count_documents({})
print("Total number of mages:", necromancers)


"""
How many thieves are there?
"""
thieves = db.RPG_Thieves.count_documents({})
print("Total number of thieves:", thieves)


"""
How many items are there?
"""
items = db.RPG_Items.count_documents({})
print("Total number of items:", items)


"""
How many weapon and non-weapon items are there?
"""
weapons = db.RPG_Weapons.count_documents({})
print('Total number of weapons:', weapons)
print('Total number of non-weapons:', items - weapons)


# """
# How many items does each character have?
# """


# """
# How many weapons does each character have?
# """


# """
# On average, how many items does each character have?
# """


# """
# On average, how many weapons does each character have?
# """
