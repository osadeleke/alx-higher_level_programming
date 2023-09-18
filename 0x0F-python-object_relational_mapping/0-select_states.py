#!/usr/bin/python3
"""List all states from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    """List all states from database hbnt_0e_0_usa
    """
    MY_HOST = 'localhost'
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(
            host=MY_HOST,
            port=MY_PORT,
            user=MY_USER,
            passwd=MY_PASS,
            db=MY_DB
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
