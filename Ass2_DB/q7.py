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
       SELECT c.first_name, c.last_name, SUM(s.price) as total_amount_spent FROM order_customer as oc
       JOIN order_shoe AS os ON oc.order_id = os.order_id
       JOIN shoe AS s ON s.shoe_id = os.shoe_id
       JOIN customer AS c ON c.customer_id = oc.customer_id
       GROUP BY oc.customer_id;
    """) 

    print (', '. join (str( row ) for row in cursor . fetchall ()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
