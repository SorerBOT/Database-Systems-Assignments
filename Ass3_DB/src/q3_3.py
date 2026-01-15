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
    # doctors(id, hospital_id, name, consultant_doctor_id, consultant_hospital_id)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                id INT,
                hospital_id INT,
                name VARCHAR(255) NOT NULL,
                consultant_doctor_id INT,
                consultant_hospital_id INT,

                PRIMARY KEY (id, hospital_id),
                FOREIGN KEY (hospital_id) REFERENCES hospitals(id),
                FOREIGN KEY (consultant_doctor_id, consultant_hospital_id) REFERENCES doctors(id, hospital_id)
                );
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
