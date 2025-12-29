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
        CREATE VIEW total_sales_per_shoe AS
        SELECT shoe.shoe_id, shoe.shoe_name, SUM(shoe.price) AS total_revenue
        FROM order_shoe
        JOIN shoe ON order_shoe.shoe_id = shoe.shoe_id
        GROUP BY shoe.shoe_id;
    """)

    # In this case, committing is optional but I prefer doing so.
    mydb.commit();

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
