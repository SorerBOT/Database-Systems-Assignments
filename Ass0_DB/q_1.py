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
               SELECT location
               FROM covid_deaths
               UNION
               SELECT location
               FROM covid_db.covid_vaccination;
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
