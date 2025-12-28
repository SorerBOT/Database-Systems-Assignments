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
               WITH SUB_TWO_MINUTES_TEAMS AS (SELECT DISTINCT l.Car
                                              FROM f1_data.fastest_laps_updated as l
                                              GROUP BY l.Car
                                              HAVING MIN(MINUTE(STR_TO_DATE(l.Time, '%i:%s.%f'))) <= 1)

               SELECT t.Car, AVG(t.PTS)
               FROM f1_data.teams_updated as t
               GROUP BY t.Car
               HAVING t.Car IN (
                   SELECT car
                   FROM SUB_TWO_MINUTES_TEAMS)
               ORDER BY AVG(t.PTS) DESC;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
