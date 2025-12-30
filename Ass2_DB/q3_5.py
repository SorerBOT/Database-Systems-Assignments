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
            INSERT INTO country (country_id, country_name)
            VALUES
                (1, 'Israel'),
                (2, 'Canada'),
                (3, 'United States'),
                (4, 'Germany'),
                (5, 'France'),
                (6, 'Japan'),
                (7, 'Australia'),
                (8, 'Italy'),
                (9, 'Spain'),
                (10, 'Brazil');
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
