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
               SELECT   Driver
               FROM     drivers_updated
               WHERE    drivers_updated.Nationality = 'ITA';
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
