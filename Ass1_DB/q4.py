# did not use LIMIT. I was afraid it needlessly sort everything O(n log n) instead of just taking the maximum in O(n).
# Simply finding the car with the most wins in 1999 and then querying for its wins in 2001
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
               SELECT COUNT(*)
               FROM f1_data.winners as w
               WHERE YEAR(Date) = 2001 AND w.Car = (
                   SELECT w.Car
                   FROM f1_data.winners as w
                   WHERE YEAR(w.Date) = 1999
                   GROUP BY w.Car
                   HAVING COUNT(*) >= ALL(
                       SELECT COUNT(*)
                       FROM f1_data.winners as w
                       WHERE YEAR(w.Date) = 1999
                       GROUP BY w.Car
                       HAVING COUNT(*)
                       )
                   );
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
