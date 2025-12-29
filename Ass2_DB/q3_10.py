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
            INSERT INTO order_customer (order_id, customer_id)
            VALUES
                (1, '123456789'),
                (2, '987654321'),
                (3, '112233445'),
                (4, '223344556'),
                (5, '334455667'),
                (6, '445566778'),
                (7, '556677889'),
                (8, '667788990'),
                (9, '778899001'),
                (10, '889900112')
    """) 
    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
