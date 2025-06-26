#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa starting with 'N'.
Takes 3 arguments: username, password, and db_name.
Results are sorted in ascending order by states.id.
Uses MySQLdb to connect to a MySQL server running on
localhost at port 3306.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor and execute the query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
