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
    # {'name': 'Anchovy', 'url': 'https://nookipedia.com/wiki/Anchovy_(fish)', 'number': '56', 'image_url': 'https://dodo.ac/np/images/7/7f/Anchovy_%28Fish%29_NH_Icon.png', 'render_url': 'https://dodo.ac/np/images/1/19/Anchovy_%28Fish%29_NH.png', 'catchphrase': 'I caught an anchovy! Stay away from my pizza!', 'catchphrase2': '', 'catchphrase3': '', 'location': 'Sea', 'shadow_size': 'Small', 'rarity': '', 'total_catch': '0', 'sell_nook': '200', 'sell_cj': '300', 'tank_width': '1', 'tank_length': '1', 'time': '4 AM – 9 PM', 'n_availability': 'All year', 's_availability': 'All year', 'catchphrases': ['I caught an anchovy! Stay away from my pizza!'], 'availability_north': [{'months': 'All year', 'time': '4 AM – 9 PM'}], 'availability_south': [{'months': 'All year', 'time': '4 AM – 9 PM'}], 'times_by_month_north': {'1': '4 AM – 9 PM', '2': '4 AM – 9 PM', '3': '4 AM – 9 PM', '4': '4 AM – 9 PM', '5': '4 AM – 9 PM', '6': '4 AM – 9 PM', '7': '4 AM – 9 PM', '8': '4 AM – 9 PM', '9': '4 AM – 9 PM', '10': '4 AM – 9 PM', '11': '4 AM – 9 PM', '12': '4 AM – 9 PM'}, 'times_by_month_south': {'1': '4 AM – 9 PM', '2': '4 AM – 9 PM', '3': '4 AM – 9 PM', '4': '4 AM – 9 PM', '5': '4 AM – 9 PM', '6': '4 AM – 9 PM', '7': '4 AM – 9 PM', '8': '4 AM – 9 PM', '9': '4 AM – 9 PM', '10': '4 AM – 9 PM', '11': '4 AM – 9 PM', '12': '4 AM – 9 PM'}, 'n_availability_array': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 's_availability_array': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']}

    name =[]
    location = []
    price = []
    rarity = []

    for d in fish_lst:
        print(d['name'])
        print(d['rarity'])
        if len(d['rarity']) == 0:
            continue
        elif len(d['rarity']) >= 1:
            name.append(d['name'])
            location.append(d['location'])
            price.append(d['sell_nook'])
            rarity.append(d['rarity'])
    # print(name)
    # print(location)
    # print(price)
    # print(rarity)
    
    #     cur.execute('CREATE TABLE IF NOT EXISTS Fish (name TEXT, number TEXT, region TEXT, month TEXT, time TEXT)')
    #     conn.commit()

    # for i in range(len(name)):
    #     cur.execute('INSERT INTO Fish (name, number, region, month, time) VALUES (?, ?, ?, ?, ?)', (name[i], number[i], 'north', north_montharray[i], n_month_times[i]))
    # conn.commit()
    # for i in range(len(name)):
    #     cur.execute('INSERT INTO Fish (name, number, region, month, time) VALUES (?, ?, ?, ?, ?)', (name[i], number[i], 'south', south_montharray[i], s_month_times[i]))
    # conn.commit()

def bugs(cur, conn):
    params = {"format": "json"}
    response = requests.get(f"https://api.nookipedia.com/nh/bugs", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})
    bug_lst = response.json()
    # print(bug_lst)


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
    # create_events_table(data)
    get_fishes(cur, conn)
    bugs(cur, conn)
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)