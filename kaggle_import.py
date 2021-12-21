import csv

import psycopg2

username = 'nedilko'
password = 'pass'
database = 'DB_lab2'

INPUT_CSV_FILE = 'fixed.csv'


query_episodes_del='''
DELETE FROM episodes CASCADE
'''

query_episodes_add='''
INSERT INTO episodes(anime_id, episodes, members) 
VALUES (%s, %s, %s)
'''

query_types_del='''
DELETE FROM types CASCADE
'''

query_types_add='''
INSERT INTO types(type_id, type_name) 
VALUES (%s, %s)
'''

query_inf_del='''
DELETE FROM anime CASCADE
'''

query_inf_add='''
INSERT INTO anime(anime_id, anime_name, type_id) 
VALUES (%s, %s, %s)
'''

query_rate_del='''
DELETE FROM ratings CASCADE
'''

query_rate_add='''
INSERT INTO ratings(anime_id, rate_value) 
VALUES (%s, %s)
'''



conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()


    cur.execute(query_episodes_del)
    cur.execute(query_rate_del)
    cur.execute(query_inf_del)
    cur.execute(query_types_del)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        # filling in types

        types = []
        for i in reader:
            types.append(i['type'])
        types=list(set(types))
        t2=[]
        for k, i in enumerate(types):
            values = (k+1, i)
            t2.append([k+1,i])
            cur.execute(query_types_add, values)
    conn.commit()

def check(val):
    for k in t2:
        if k[1] == val:
            return k[0]



with conn:
    cur = conn.cursor()
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
#         filling in anime table

        for idx, row in enumerate(reader):
            values = (idx+1, row['name'], check(row['type']))
            cur.execute(query_inf_add, values)
    conn.commit()

with conn:
    cur = conn.cursor()
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        # filling in episodes
        for idx, row in enumerate(reader):
            values = (idx+1, row['episodes'], row['members'])
            cur.execute(query_episodes_add, values)
    conn.commit()

with conn:
    cur = conn.cursor()
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
#             filling in rate table
        for idx, row in enumerate(reader):
            values = (idx+1, row['rating'])
            cur.execute(query_rate_add, values)
    conn.commit()



# # #
# cur.execute('SELECT * FROM anime')
# for row in cur:
#     print(row)
#
# cur.execute('SELECT * FROM types')
# for row in cur:
#     print(row)
#
# cur.execute('SELECT * FROM ratings')
# for row in cur:
#     print(row)
#
# cur.execute('SELECT * FROM episodes')
# for row in cur:
#     print(row)

