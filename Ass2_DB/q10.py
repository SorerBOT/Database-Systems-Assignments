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
        WITH inventory_shoes AS (
            SELECT shoe_name FROM shoe
        ),
        upcoming_collections AS (
            SELECT collection_name FROM upcoming
        )
        (
            SELECT shoe_name AS name, "Inventory" AS source
            FROM inventory_shoes
        )
        UNION
        (
            SELECT collection_name AS name, "Upcoming Release" AS source
            FROM upcoming_collections
        );
    """)

    print (', '. join (str( row ) for row in cursor . fetchall ()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
