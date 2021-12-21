import json
import psycopg2

username = 'nedilko'
password = 'pass'
database = 'DB_lab2'

file_name = 'nedilko_DB_{}.csv'
TABLES = [
    'information',
    'types',
    'episodes',
    'rates'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)
data = {}
with conn:
    cur = conn.cursor()

    for table in ('anime', 'types', 'episodes', 'ratings'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        field = [x[0] for x in cur.description]
    for row in cur:
        rows.append(dict(zip(field, row)))
    data[table] = rows
    with open('data.json', 'w') as final:
        json.dump(data, final, default=str)
