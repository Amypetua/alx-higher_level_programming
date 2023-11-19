#!/usr/bin/python3
"""
A script that lists all cities from a database
"""

import MySQLdb
import sys


if __name__ == '__main__':

    db  = MySQldb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
