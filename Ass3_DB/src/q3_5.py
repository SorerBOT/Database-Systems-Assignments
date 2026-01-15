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
    ## diseases(id, name, medicine_id, severity)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS diseases (
                    id INT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    medicine_id INT,
                    severity INT,

                    FOREIGN KEY (medicine_id) REFERENCES medicines(id)
                );
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
