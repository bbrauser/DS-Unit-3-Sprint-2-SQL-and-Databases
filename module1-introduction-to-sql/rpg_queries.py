# Imports
import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = """
    SELECT *
    FROM charactercreator_character;
"""


if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results)


"""
How many total characters are there?
"""
query_total = 'SELECT COUNT(*) FROM charactercreator_character;'
tot_char = execute_query(curs, query_total)
print("Total number of characters:", tot_char[0][0])


"""
How many clerics are there?
"""
query_cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
clerics = execute_query(curs, query_cleric)
print("- Clerics:", clerics[0][0])


"""
How many fighers are there?
"""
query_fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
fighters = execute_query(curs, query_fighter)
print("- Fighters:", fighters[0][0])


"""
How many mages are there?
"""
query_mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
mages = execute_query(curs, query_mage)
print("- Mages:", mages[0][0])


"""
How many necromancers are there?
"""
query_necromancers = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
necromancers = execute_query(curs, query_necromancers)
print("- Necromancers:", necromancers[0][0])


"""
How many thieves are there?
"""
query_thieves = 'SELECT COUNT(*) FROM charactercreator_thief;'
thieves = execute_query(curs, query_thieves)
print("- Thieves:", thieves[0][0])


"""
How many items are there?
"""
query_items = 'SELECT COUNT(*) FROM armory_item;'
items = execute_query(curs, query_items)
print("Total number of items:", items[0][0])


"""
How many weapon and non-weapon items are there?
"""
query_weapons = 'SELECT COUNT(*) FROM armory_weapon;'
weapons = execute_query(curs, query_weapons)
print("- Non-weapon items:", (items[0][0] - weapons[0][0]))
print("- Weapons:", weapons[0][0])


"""
How many items does each character have?
"""
character_items_20 = """
    SELECT character_id, name, COUNT(item_id) FROM
    (SELECT cc.character_id, cc.name, ai.item_id, ai.name
    FROM charactercreator_character AS cc,
    armory_item AS ai, charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND ai.item_id = cci.item_id)
    GROUP BY 1 ORDER BY 3 DESC
    LIMIT 20;
"""
tot_char_items = execute_query(curs, character_items_20)
print(tot_char_items)


"""
How many weapons does each character have?
"""
character_weapons_20 = """
    SELECT name, COUNT(item_ptr_id) FROM
    (SELECT cc.character_id, cc.name, aw.item_ptr_id, aw.power
    FROM charactercreator_character AS cc,
    armory_weapon AS aw,
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND aw.item_ptr_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC
    LIMIT 20;
"""
tot_char_weapons = execute_query(curs, character_weapons_20)
print(tot_char_weapons)


"""
On average, how many items does each character have?
"""
# Option 1
avg_num_items_per_character = """
    SELECT AVG(total_items) AS avg_num_items_per_character FROM 
	(SELECT name, COUNT(item_id) AS total_items FROM
    (SELECT cc.character_id, cc.name, ai.item_id
    FROM charactercreator_character AS cc,
    armory_item AS ai,
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND ai.item_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC);
"""
avg_char_items = execute_query(curs, avg_num_items_per_character)
print("Average number of items (Option 1):", avg_char_items[0][0])


# Option 2
avg_num_items_per_character2 = """
    SELECT cast(COUNT(charactercreator_character_inventory.item_id) as float)/
    COUNT(DISTINCT character_id)
    FROM charactercreator_character_inventory
    INNER JOIN armory_item
    ON armory_item.item_id = charactercreator_character_inventory.item_id;
"""
avg_char_items2 = execute_query(curs, avg_num_items_per_character2)
print("Average number of items (Option 2):", avg_char_items2[0][0])


"""
On average, how many weapons does each character have?
"""
# Option 1
avg_num_weapons_per_character = """
    SELECT AVG(total_weapons) AS avg_num_weapons_per_character FROM 
	(SELECT name, COUNT(item_ptr_id) AS total_weapons FROM
    (SELECT cc.character_id, cc.name, aw.item_ptr_id, aw.power
    FROM charactercreator_character AS cc,
    armory_weapon AS aw,
    charactercreator_character_inventory AS cci
    WHERE cc.character_id = cci.character_id
    AND aw.item_ptr_id = cci.item_id)
    GROUP BY 1 ORDER BY 2 DESC);
"""
avg_char_weapons = execute_query(curs, avg_num_weapons_per_character)
print("Average number of weapons (Option 1):", avg_char_weapons[0][0])


# Option 2
avg_num_weapons_per_character2 = """
    SELECT cast(COUNT(charactercreator_character_inventory.item_id) as float)/
    COUNT(DISTINCT character_id)
    FROM charactercreator_character_inventory
    INNER JOIN armory_weapon
    ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id;
"""
avg_char_weapons2 = execute_query(curs, avg_num_weapons_per_character2)
print("Average number of weapons (Option 2):", avg_char_weapons2[0][0])