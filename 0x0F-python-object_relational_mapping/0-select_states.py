#!/usr/bin/python3
import MySQLdb
import sys

MY_HOST = 'localhost'
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
