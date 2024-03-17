#!/usr/bin/python3
"""
List values that match argument safe from mysql
injection
"""
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], port=3306)

    mouse = connection.cursor()
    mouse.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    Nstates = mouse.fetchall()

    for Nstate in Nstates:
        print(Nstate)
