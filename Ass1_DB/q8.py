# just calculating the two sums and returning the difference. Using CTEs to store the data

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
               WITH
               FERRARI_PTS AS (
                   SELECT SUM(PTS) AS total
                   FROM f1_data.teams_updated
                   WHERE Car = 'Ferrari'
                   ),
               MASERATI_PTS AS (
                   SELECT SUM(PTS) as total	
                   FROM f1_data.teams_updated
                   WHERE Car = 'Maserati')

               SELECT
               (SELECT total FROM FERRARI_PTS) -
               (SELECT total FROM MASERATI_PTS) AS diff;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
