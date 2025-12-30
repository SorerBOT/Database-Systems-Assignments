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
        SELECT DISTINCT shoe.shoe_name
        FROM shoe
        LEFT JOIN order_shoe ON shoe.shoe_id = order_shoe.shoe_id
        WHERE order_shoe.order_id IS NULL;
    """)

    print (', '. join (str( row ) for row in cursor.fetchall()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
