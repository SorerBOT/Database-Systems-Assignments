import mysql.connector
if name == ' main ':
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="covid_db",
            port='3307',
            )

cursor = mydb.cursor()
cursor.execute("""
               SELECT date, new_cases
               FROM covid_deaths
               WHERE location='south america' AND new_cases > 150000
               ORDER BY new_cases ASC;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
