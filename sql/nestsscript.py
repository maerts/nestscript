import re
import datetime
import os
import traceback
import MySQLdb
import logging
import requests
import gc
import json
from datetime import date

# Initialize db
db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='nestscript')
c = db.cursor()

# Truncate nest table
c.execute ("""Truncate nestscript.nest;""")

# Get the nest information from the json file.
with open('/var/local/data/nests.stats.json') as data_file:    
    nests = json.load(data_file)

c = db.cursor()
# loop through the nest info and insert rows.
for nest in nests:
    # every row has pid, lng, lat, c, et, st
    print(nest)
    try:
        query = "INSERT INTO nestscript.nest (`pokemon_id`, `lat`, `lng`, `c`, `st`, `et`) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (int(nest['pid']), float(nest['lat']), float(nest['lng']), int(nest['c']), int(nest['st']), int(nest['et']),)
        c.execute(query, data)
        db.commit()
    except:
        print('error')

c.close()
db.close()