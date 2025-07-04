#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and DB name from command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute SQL query to fetch all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and print them
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
