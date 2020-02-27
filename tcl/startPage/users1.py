import sqlite3

conn = sqlite3.connect('user3.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE USERS
         (
         username       TEXT PRIMARY KEY   NOT NULL,
         password      TEXT               NOT NULL
         );''')
print("Table created successfully");

conn.close()