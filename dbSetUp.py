import sqlite3

conn = sqlite3.connect('AAbox.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE USERS
         (
         username       TEXT PRIMARY KEY   NOT NULL,
         password      TEXT               NOT NULL,
         city      TEXT               NOT NULL,
         birth_year      TEXT               NOT NULL,
         mothers_name      TEXT               NOT NULL
         );''')
print("Users Table created successfully");
conn.execute('''CREATE TABLE GAMES
         (
         username TEXT NOT NULL,
         game_id   INTEGER NOT NULL,
         score    INTEGER NOT NULL,
         PRIMARY KEY (username, game_id)
         );''')
print("Games Table created successfully");
conn.close()