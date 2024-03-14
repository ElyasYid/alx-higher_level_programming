#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3], port=3306)

    tred = database.cursor()
    tred.execute("SELECT * FROM states;")
    states = tred.fetchall()

    for state in states:
        print(state)
