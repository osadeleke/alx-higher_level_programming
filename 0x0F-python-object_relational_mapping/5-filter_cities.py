#!/usr/bin/python3
"""List all cities with state name from argument
from database hbtn_0e_0_usa safe from MySQL injections
"""
import MySQLdb
import sys


def main():
    """List all cities with state name from argument
    from database hbnt_0e_0_usa safe from MySQL injections
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
    firstQ = "SELECT cities.name FROM cities JOIN states ON cities.state_id"
    secQ = "= states.id WHERE states.name = %s ORDER BY cities.id ASC"
    finalQuery = firstQ + secQ
    cur.execute(finalQuery, (MY_ARG,))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        for col in row:
            cities.append(col)
    cityList = ', '.join(cities)
    print(cityList)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
