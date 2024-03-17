#!/usr/bin/python3
"""
Lists values in table that match provided arg
"""
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    mouse = connection.cursor()
    mouse.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    matches = mouse.fetchall()

    for match in matches:
        print(match)
