#!/usr/bin/python3
"""List all cities of a given state."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and list cities for the given state."""
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
