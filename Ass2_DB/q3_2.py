import mysql.connector

if __name__ == '__main__':
    # Establish the connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )

    # Create a cursor object to execute queries
    cursor = mydb.cursor()

    ## Execute the SQL query
    # (shoe_id, size_id) combinations are unique
    # shoe_id and size_id are foreign keys

    cursor.execute("""
            INSERT INTO size (size_id, european_number, us_number)
            VALUES
               (1, 38, 6),
               (2, 39, 7),
               (3, 40, 8),
               (4, 41, 9),
               (5, 42, 10),
               (6, 43, 11),
               (7, 44, 12),
               (8, 45, 13),
               (9, 46, 14),
               (10, 47, 15),
               (11, 36, 4),
               (12, 37, 5),
               (13, 48, 16),
               (14, 49, 17),
               (15, 50, 18)
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
