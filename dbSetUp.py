import sqlite3

conn = sqlite3.connect('AAbox.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE USERS
         (
         username       TEXT PRIMARY KEY   NOT NULL,
         password      TEXT               NOT NULL,
         city      TEXT               NOT NULL,
         birthYear      TEXT               NOT NULL,
         mothersName      TEXT               NOT NULL
         );''')
print("Users Table created successfully");
conn.execute('''CREATE TABLE GAMES
         (
         username TEXT NOT NULL,
         gameID   INTEGER NOT NULL,
         score    INTEGER NOT NULL,
         PRIMARY KEY (username, gameID)
         );''')
print("Games Table created successfully");
conn.close()