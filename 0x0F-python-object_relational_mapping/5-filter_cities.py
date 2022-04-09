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
    cur.execute("""SELECT cities.name
                 FROM states INNER JOIN cities ON states.id=cities.state_id
                 WHERE states.name LIKE %s""", (argv[4],))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i == (len(rows) - 1):
            print(str(rows[i][0]))
        else:
            print(str(rows[i][0]) + ', ', end='')
    if (not rows):
        print()

    cur.close()
    db.close()
