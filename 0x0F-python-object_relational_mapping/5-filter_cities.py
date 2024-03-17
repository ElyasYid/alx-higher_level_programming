#!/usr/bin/python3
"""
List all cities of a state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], port=3306)

    mouse = connection.cursor()
    mouse.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    cities = mouse.fetchall()

    print(", ".join([city[1] for city in cities]))
