import sqlite3
import pandas as pd

df = pd.read_csv('ml-latest-small/ratings.csv', encoding='utf8')
conn = sqlite3.connect('data.db')
c = conn.cursor()

# creating users table and populate with data
c.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, user_name TEXT, user_password TEXT)")
conn.commit()

sql = 'INSERT INTO users VALUES (NULL, ?, ?)'
c.execute(sql, ('user', 'password'))
conn.commit()
print('User created successfully!')

# creating users table and populate with data
c.execute("CREATE TABLE ratings (user_id TEXT, movie_id TEXT, rating FLOAT, timestamp STRING)")
conn.commit()

sql = 'INSERT INTO ratings VALUES (?, ?, ?, ?)'

data = df.itertuples(index=False, name=None)

for d in data:
    c.execute(sql, d)
    conn.commit()
conn.close()
print('Ratings table in data.db created successfully!')

df = pd.read_csv('ml-latest-small/movies.csv', encoding='utf8')
conn = sqlite3.connect('data.db')
c = conn.cursor()

# creating users table and populate with data
c.execute("CREATE TABLE movies (movie_id TEXT, title TEXT, genres TEXT)")
conn.commit()

sql = 'INSERT INTO movies VALUES (?, ?, ?)'

data = df.itertuples(index=False, name=None)

for d in data:
    c.execute(sql, d)
    conn.commit()
conn.close()
print('Movies table in data.db created successfully!')
