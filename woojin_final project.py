import json
import unittest
import os
import requests
import sqlite3
import os
import matplotlib.pyplot as plt

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_events(link):
    params = {"date": "2022-05-01", "year":"2022", "month": "May", "day":1, "format": "json"}

    response = requests.get(f"https://api.nookipedia.com/nh/events", params=params, headers={"Accept-Version": "1.0.0", "X-API-KEY":"55812024-1e72-4393-989e-9669fe7e2c0f"})

    # {'event': "Don Resetti's birthday", 'date': '2022-05-01', 'type': 'Birthday', 'url': 'https://nookipedia.com/wiki/Don_Resetti'}, 
    # {'event': "Don's birthday", 'date': '2022-05-01', 'type': 'Birthday', 'url': 'https://nookipedia.com/wiki/Don_Resetti'}, 
    # {'event': "Mother's Day Nook Shopping event begins", 'date': '2022-05-01', 'type': 'Nook Shopping', 'url': 'https://nookipedia.com/wiki/Nook_Shopping_seasonal_event'}, 
    # {'event': 'Mushroom recipes become available (Southern Hemisphere)', 'date': '2022-05-01', 'type': 'Recipes', 'url': 'https://nookipedia.com/wiki/DIY_recipes/Autumn'}, 
    # {'event': "Clyde's birthday", 'date': '2022-05-01', 'type': 'Birthday', 'url': 'https://nookipedia.com/wiki/Clyde'}

    print (type(response.json()))
    print(response.json())

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
    link = "https://api.nookipedia.com/villagers"
    # 55812024-1e72-4393-989e-9669fe7e2c0f"
    data = get_events(link)
    create_events_table(data)
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)


