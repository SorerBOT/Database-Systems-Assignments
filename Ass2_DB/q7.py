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
        SELECT customer.first_name, customer.last_name, COALESCE(SUM(s.price), 0) as total_amount_spent
        FROM customer
        LEFT JOIN order_customer ON order_customer.customer_id = customer.customer_id
        LEFT JOIN order_shoe ON order_customer.order_id = order_shoe.order_id
        LEFT JOIN shoe ON shoe.shoe_id = order_shoe.shoe_id
        GROUP BY customer.customer_id;
    """) 

    print (', '. join (str( row ) for row in cursor . fetchall ()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
