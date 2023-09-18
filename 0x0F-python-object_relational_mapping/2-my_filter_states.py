#!/usr/bin/python3
"""List all states with names from argument
from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    """List all states with names from argument
    from database hbnt_0e_0_usa
    """
    MY_HOST = 'localhost'
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_ARG = sys.argv[4]
    db = MySQLdb.connect(
            host=MY_HOST,
            port=MY_PORT,
            user=MY_USER,
            passwd=MY_PASS,
            db=MY_DB
    )
    cur = db.cursor()
    firstQuery = "SELECT id, name FROM states WHERE name "
    secondQuery = "= '{}' ORDER BY id ASC".format(MY_ARG)
    finalQuery = firstQuery + secondQuery
    cur.execute(finalQuery)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
