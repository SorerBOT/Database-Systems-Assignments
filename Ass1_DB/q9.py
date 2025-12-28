# calculating sum of points earned by each driver, then grouping them by their nationality and at last taking the avg across the each group
# afterwards, using two more CTEs to calculate the fastest lap and most recent victories.
# using OUTER JOINs in order to return something for each nationality even if no driver from that nationality has ever won, or that they have no recorded laps

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
               AVG_PTS AS (
                   SELECT nationality, AVG(total_pts) AS avg_pts
                   FROM (
                       SELECT Driver AS driver, Nationality as nationality, SUM(PTS) as total_pts
                       FROM f1_data.drivers_updated
                       GROUP BY Driver, Nationality) AS gd
                   GROUP BY gd.nationality),
               FASTEST_LAP AS (
                   SELECT gd.Nationality AS nationality, MIN(dmt.min_time) AS fastest_lap
                   FROM (
                       SELECT Driver as driver, MIN(Time) as min_time
                       FROM fastest_laps_updated
                       GROUP BY Driver
                       ) AS dmt JOIN f1_data.drivers_updated AS gd ON (dmt.driver = gd.Driver)
                   GROUP BY gd.Nationality
                   ),
               MOST_RECENT_WIN AS (
                   SELECT d.Nationality AS nationality, MAX(w.Date) as most_recent
                   FROM f1_data.winners as w JOIN f1_data.drivers_updated as d
                   ON w.Winner = d.Driver
                   GROUP BY d.Nationality
                   )

               SELECT d_avg.nationality as Nationality, d_avg.avg_pts as avg_pts, d_fastest.fastest_lap, d_recent.most_recent
               FROM ((AVG_PTS as d_avg LEFT JOIN FASTEST_LAP as d_fastest
                      ON d_avg.nationality = d_fastest.nationality)
                     LEFT JOIN MOST_RECENT_WIN as d_recent ON d_avg.nationality = d_recent.nationality)
               """)
print(', '.join(str(row) for row in cursor.fetchall()))
