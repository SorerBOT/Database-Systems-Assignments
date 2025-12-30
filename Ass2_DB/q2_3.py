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
        CREATE TABLE IF NOT EXISTS shoe_size (
            shoe_id INT,
            size_id INT,

            PRIMARY KEY (shoe_id, size_id),
            FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
            FOREIGN KEY (size_id) REFERENCES size(size_id)
        );
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
