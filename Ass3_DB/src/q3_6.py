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
    ## patients(id, name, height, weight, is_male, doctor_id, hospital_id, disease_previous_id, disease_new_id)
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                    id INT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    height INT NOT NULL,
                    weight INT NOT NULL,
                    is_male BOOLEAN NOT NULL,
                    doctor_id INT NOT NULL,
                    hospital_id INT NOT NULL,
                    disease_previous_id INT,
                    disease_new_id INT NOT NULL,

                    FOREIGN KEY (doctor_id, hospital_id) REFERENCES doctors(id, hospital_id),
                    FOREIGN KEY (disease_previous_id) REFERENCES diseases(id),
                    FOREIGN KEY (disease_new_id) REFERENCES diseases(id)
                );
    """)

    ## !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    ## Close the cursor and the connection
    cursor.close()
    mydb.close()
