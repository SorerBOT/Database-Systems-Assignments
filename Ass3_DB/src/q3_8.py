import mysql.connector

if __name__ == '__main__':
    # Establish the connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hosppdd",
        port='3307',
    )

    # Create a cursor object to execute queries
    cursor = mydb.cursor()

    ## Execute the SQL query
    ## opinion(id, comment)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS opinion (
                    id INT PRIMARY KEY,
                    comment TEXT NOT NULL,

                    FOREIGN KEY (id) REFERENCES ratings(id)
                );
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
