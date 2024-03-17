#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], port=3306)

    mouse = connection.cursor()
    mouse.execute("SELECT * FROM states;")
    states = mouse.fetchall()

    for state in states:
        print(state)
