#!/usr/bin/python3
"""List all states from a database that start with the letter N."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and print states starting with 'N'."""
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
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC;"
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
