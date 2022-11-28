import json
import unittest
import os
import requests
import sqlite3

# Name: Zeinab Ghandour
# Email: zghandou@umich.edu
# ID: 84727401


API_KEY = "https://acnhapi.com/v1/"

def read_json(cache_filename):
    try: 
        file = open(cache_filename, 'r')
        string= file.read() 
        file.close()
        data = json.loads(string)
        #print(data)
        return data

    except:
        dict = {} 
        return dict

def write_json(cache_filename, dict):
    with open(cache_filename, 'w') as f:
        j =json.dumps(dict)
        f.write(j)

def make_villager_table(data, cur, conn):

    cur.execute("DROP TABLE IF EXISTS Villager") 
    cur.execute("CREATE TABLE IF NOT EXISTS Villager (name TEXT UNIQUE PRIMARY KEY,\
        gender_id INTEGER, birthday INTEGER, species INTEGER, personality INTEGER, hobby INTEGER)")
    
    for i in data: 
        name = i["name"]['name-USen']
        type_name = i["type"][0]
        cur.execute("SELECT id FROM Types WHERE type = ?" ,(type_name,)) 
        type_id = int(cur.fetchone()[0])
        birthday= int(i["base"]["HP"])
        species = int(i["base"]["Attack"])
        personality = int(i["base"]["Defense"])
        hobby = int(i["base"]["Speed"])

        cur.execute("INSERT INTO Pokemon (name, type_id,HP,attack,defense,speed) VALUES(?,?,?,?,?,?)",\
            )

    conn.commit()

'''def get_request_url(list):

    date = "2016-07-10"
    url = f"https://acnhapi.com/v1/{villagerID}"

    return url '''
