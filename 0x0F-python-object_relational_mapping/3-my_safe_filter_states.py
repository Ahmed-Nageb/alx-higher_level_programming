#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    db.close()
