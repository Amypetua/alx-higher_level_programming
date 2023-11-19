#!/usr/bin/python3
"""Script that list all states from a database"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
