import json
import unittest
import os
import requests
import sqlite3
import os
import matplotlib.pyplot as plt

#import [filename] as [name]

#reference functions from the file
#filename.function

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_events(cur, conn):
    # params = {"date": "2022-05-01", "year":"2022", "month": "May", "day":1, "format": "json"}
    params = {"format": "json"}

    response = requests.get(f"https://api.nookipedia.com/nh/events", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})

    events_lst = response.json()
    # print(events_lst)

    type_lst = []
    event_lst = []
    date_lst = []

    for d in events_lst:
        if d["type"] == 'Event' or d["type"] == 'Season':
            event_lst.append(d['event'])
            date_lst.append(d['date'])
            type_lst.append(d['type'])
            cur.execute('CREATE TABLE IF NOT EXISTS Events (event TEXT, date TEXT, event_type TEXT)')
            conn.commit()

    for i in range(len(type_lst)):
        cur.execute('INSERT INTO Events (event, date, event_type) VALUES (?, ?, ?)', (event_lst[i], date_lst[i], type_lst[i]))
    conn.commit()



def create_events_table(cur, conn, list):
    for d in list:
        pass






####################
#### TEST CASES ####
####################

# class TestHomework6(unittest.TestCase):
#     def setUp(self):
#         pass

def main():
    cur, conn = setUpDatabase('events.db')
    # link = "https://api.nookipedia.com/villagers"
    # 55812024-1e72-4393-989e-9669fe7e2c0f"
    data = get_events(cur, conn)
    create_events_table(data)
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)


