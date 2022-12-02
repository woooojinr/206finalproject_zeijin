import json
import unittest
import os
import requests
import sqlite3

# Name: Zeinab Ghandour
# Email: zghandou@umich.edu
# ID: 84727401


'''API_KEY = "https://acnhapi.com/v1/"


def write_json(cache_filename, dict):
    with open(cache_filename, 'w') as f:
        j =json.dumps(dict)
        f.write(j)

'''
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

    
def get_data(villager_id):

    link = f"http://acnhapi.com/v1/villagers/{villager_id}"
    response = requests.get(link)
    r = response.text
    data = json.loads(r)

    #make_villager_table(data, cur, conn)
    #print(data)

    return data 

def create_villager_table(cur, conn):
     cur.execute("CREATE TABLE IF NOT EXISTS Villager (name TEXT UNIQUE PRIMARY KEY,\
        gender_id INTEGER, birthday_string STRING, species STRING, personality STRING, hobby STRING)")
    
    
def make_gender_table(data, cur, conn):
    gender_list = []

    for villager in data:
        gender_type = villager['gender']
            #print(gender_type)
        if gender_type not in gender_list:
            g = gender_list.append(gender_type)
            #print(g)
            
    cur.execute("CREATE TABLE IF NOT EXISTS Gender (id INTEGER PRIMARY KEY, gender TEXT UNIQUE)")
    for i in range(len(gender_list)):
        cur.execute("INSERT OR IGNORE INTO Gender (id,gender) VALUES (?,?)",(i,gender_list[i]))
    conn.commit()

def add_villager(data, cur, conn):

    #cur.execute("CREATE TABLE IF NOT EXISTS Villager (name TEXT UNIQUE PRIMARY KEY,\
        #gender_id INTEGER, birthday_string STRING, species STRING, personality STRING, hobby STRING)")
    
    for i in data: 
        name = i["name"]['name-USen']
        gender_name = i["gender"]
        cur.execute("SELECT id FROM Gender WHERE gender = ?" ,(gender_name,)) 
        gender_id = int(cur.fetchone()[0])
        birthday_string= i["birthday-string"]
        species = i[ "species"]
        personality = i["personality"]
        hobby = i["hobby"]

        cur.execute("INSERT INTO Villager (name, gender_id, birthday_string, species, personality, hobby) VALUES(?,?,?,?,?,?)",\
            (name, gender_id, birthday_string, species, personality, hobby))

    conn.commit()
    

def main():
    cur, conn = setUpDatabase('villagers.db')
    #make a loop to call first function, make the count villager id num

    stuff = []
    for x in range(1,26):
        stuff.append(get_data(x))

    cur, conn = setUpDatabase('villagers.db')
    create_villager_table(cur, conn)
    make_gender_table(stuff, cur, conn)
    add_villager(stuff, cur, conn)
    
    conn.close()

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)

