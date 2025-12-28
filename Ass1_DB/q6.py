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
               SELECT DISTINCT GP1.`Grand Prix` AS GP1, GP2.`Grand Prix` AS GP2, GP1.Laps AS Laps
               FROM f1_data.winners AS GP1 JOIN f1_data.winners AS GP2
               ON(GP1.Laps = GP2.Laps AND GP1.`Grand Prix` < GP2.`Grand Prix`)
               WHERE GP1.Laps >= 80;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
