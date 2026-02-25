#!/usr/bin/python3
"""List all states from the database that don't start with N."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and print states not starting with 'N'."""
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE name NOT LIKE 'N%' "
        "ORDER BY id ASC;"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
