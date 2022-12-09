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

# def get_events(cur, conn):
#     # params = {"date": "2022-05-01", "year":"2022", "month": "May", "day":1, "format": "json"}
#     params = {"format": "json"}
#     response = requests.get(f"https://api.nookipedia.com/nh/events", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})

#     events_lst = response.json()
#     type_lst = []
#     event_lst = []
#     date_lst = []

#     for d in events_lst:
#         if d["type"] == 'Event' or d["type"] == 'Season':
#             event_lst.append(d['event'])
#             date_lst.append(d['date'])
#             type_lst.append(d['type'])
#             cur.execute('CREATE TABLE IF NOT EXISTS Events (id INTEGER PRIMARY KEY, event TEXT, date TEXT, event_type TEXT)')
#             conn.commit()

#     for i in range(len(type_lst)):
#         cur.execute('INSERT OR IGNORE INTO Events (id, event, date, event_type) VALUES (?, ?, ?, ?)', (i, event_lst[i], date_lst[i], type_lst[i]))
#     conn.commit()

def get_fishes(cur, conn):
    params = {"format": "json"}
    response = requests.get(f"https://api.nookipedia.com/nh/fish", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})

    fish_lst = response.json()
    print(fish_lst)

    name = []
    number = []
    north_montharray = []
    n_month_times = []
    south_montharray = []
    s_month_times = []

    for d in fish_lst:
        name.append(d['name'])
        number.append(d['number'])
        for k in (d['times_by_month_north']).keys():
            north_montharray.append(k)
            n_month_times.append(d['times_by_month_north'][k])
        for k in (d['times_by_month_south']).keys():
            south_montharray.append(k)
            s_month_times.append(d['times_by_month_south'][k])
    # print(north_montharray)
    # print(n_month_times)
        cur.execute('CREATE TABLE IF NOT EXISTS Fish (name TEXT, number TEXT, region TEXT, month TEXT, time TEXT)')
        conn.commit()

    for i in range(len(name)):
        cur.execute('INSERT INTO Fish (name, number, region, month, time) VALUES (?, ?, ?, ?, ?)', (name[i], number[i], 'north', north_montharray[i], n_month_times[i]))
    conn.commit()
    for i in range(len(name)):
        cur.execute('INSERT INTO Fish (name, number, region, month, time) VALUES (?, ?, ?, ?, ?)', (name[i], number[i], 'south', south_montharray[i], s_month_times[i]))
    conn.commit()

def bugs(cur, conn):
    params = {"format": "json"}
    response = requests.get(f"https://api.nookipedia.com/nh/bugs", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})
    bug_lst = response.json()
    # print(bug_lst)

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
    cur, conn = setUpDatabase('ACinfo.db')
    # link = "https://api.nookipedia.com/villagers"
    # 55812024-1e72-4393-989e-9669fe7e2c0f"
    data = get_events(cur, conn)
    # create_events_table(data)
    get_fishes(cur, conn)
    bugs(cur, conn)
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)