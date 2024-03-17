#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], port=3306)

    mouse = connection.cursor()
    mouse.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    cities = mouse.fetchall()

    for city in cities:
        print(city)
