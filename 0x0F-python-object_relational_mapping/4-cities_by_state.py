#!/usr/bin/python3
"""
MySQLdb script that lists all states from dB.
"""

import MySQLdb
from sys import argv

if len(argv) > 3:
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM states
                 INNER JOIN cities ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
