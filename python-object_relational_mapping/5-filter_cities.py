#!/usr/bin/python3
"""Script that lists all cities of a given state from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Bazaya qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # SQL sorğusu - SQL Injection-a qarşı %s istifadə olunur
    query = ("SELECT cities.id, cities.name, states.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = BINARY %s "
             "ORDER BY cities.id ASC")

    # İkinci arqument olaraq axtarılan ştatın adını ötürürük
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()
