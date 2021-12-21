import csv
import psycopg2


username = 'nedilko'
password = 'pass'
database = 'DB_lab2'

file_name = 'nedilko_DB_{}.csv'
TABLES = [
    'anime',
    'types',
    'episodes',
    'ratings'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)
with conn:
    cur = conn.cursor()
    for name in TABLES:
        cur.execute('SELECT * FROM ' + name)
        field = [x[0] for x in cur.description]
        with open(file_name.format(name), 'w') as final:
            writer = csv.writer(final)
            writer.writerow(field)
            for row in cur:
                writer.writerow([str(x) for x in row])