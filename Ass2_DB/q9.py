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

    cursor.execute("""
        SELECT shoe.shoe_name, COUNT(shoe_size.shoe_id) AS amount_sizes_available
        FROM shoe
        LEFT JOIN shoe_size on shoe.shoe_id = shoe_size.shoe_id
        GROUP BY shoe.shoe_id;
    """)

    print (', '. join (str( row ) for row in cursor . fetchall ()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
