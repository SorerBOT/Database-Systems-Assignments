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
        SELECT size.european_number, us_number, AVG(shoe.price) AS average_price
        FROM size
        JOIN shoe_size ON size.size_id = shoe_size.size_id
        JOIN shoe ON shoe.shoe_id = shoe_size.shoe_id
        GROUP BY size.size_id
        ORDER BY average_price DESC;
    """) 

    print (', '. join (str( row ) for row in cursor.fetchall ()))

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
