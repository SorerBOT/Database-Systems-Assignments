import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="f1_data",
            port='3307',
            )
cursor = mydb.cursor()
cursor.execute("""
               ((SELECT Driver as driver
                 FROM f1_data.drivers_updated
                 WHERE Nationality = 'ARG')
                UNION
                (SELECT Winner as driver
                 FROM f1_data.winners
                 WHERE Car = 'Ferrari'))
               ORDER BY driver ASC;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
