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
    # Print results in comma delimited format
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
