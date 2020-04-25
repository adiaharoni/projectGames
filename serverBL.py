import sqlite3
import sys

want_to_play = {}
dbName = "Abox.db"

def register(username, password, city, birthYear, mothersName):
    print("register")
    conn = sqlite3.connect(dbName)
    cursor = conn.execute("SELECT * from users where username= '" + username + "' ")
    rows = cursor.fetchall()
    if len(rows) != 0:
        return 1 #error: Username already exists
    if len(password)<4:
        return 2 #error: password length <4
    elif city== "":
        ret=3 #error: empty city
    elif not birthYear.isdigit():
        return 4 #error: year in valid
    elif int(birthYear)< 1900 or int(birthYear)> 2020 : #the year should be between 1900-2020
        return 4 #error: year in valid
    elif mothersName== "":
        return 5 #error: empty mother name
    else:
        cursor = conn.execute("INSERT INTO USERS (username,password,city,birthYear,mothersName) \
                                            VALUES ('" + username + "', '" + password + "', '" + city + "', '" + birthYear + "', '" + mothersName + "' )")
        conn.commit()
        conn.close()
        sys.stdout.flush()
        return 0 #ok

def login(username, password):
    print("login")
    conn = sqlite3.connect(dbName)
    cursor = conn.execute(
        "SELECT * from USERS where username= '" + username + "' and password= '" + password + "'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not in db! "+ username+" should re-register")
        return 6 #error: wrong username or password
    else:
        print(username+" is in db!")
        return 0 #ok
    conn.close()
    sys.stdout.flush()
    return ret

def forgotPassword(username, city, birthYear, mothersName):
    print("forgotPassword")
    query = "SELECT * from USERS where username= '" + username + "' and city= '" + city + "' and birthYear= '" + birthYear + "' and mothersName= '" + mothersName + "'"
    print("query = ", query, "\n")
    conn = sqlite3.connect('Abox.db')
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    password = ""
    ret = 0
    if len(rows) == 0:
        print("not in db! you should re-register")
        ret = 7 #error: user not found
    else:
        print("read password")
        for row in rows:
            print("in cursor")
            password = row[1]
            print("password = ", password, "\n")
            ret = 0 #ok
    conn.commit()
    conn.close()
    sys.stdout.flush()
    return ret, password

def wantToPlay(username, gameID, gameNumber):
    if gameID in want_to_play.keys():
        (username1, gameNumber1) = want_to_play[gameID]

        query = "SELECT * from GAMES where username in ( '" + username1 + "' ,  '" + username + "' ) and gameID = " + gameID
        print("query = ", query, "\n")
        conn = sqlite3.connect('Abox.db')
        cursor = conn.execute(query)
        rows = cursor.fetchall()
        score = 0
        score1 = 0
        if len(rows) == 0:
            print("no scores in db")
        else:
            for row in rows:
                print("in cursor")
                db_username = row[0]
                if db_username == username:
                    score = row[2]
                else:
                    score1 = row[2]
        conn.commit()
        conn.close()
        sys.stdout.flush()

        del want_to_play[gameID]
        return 9, username, score, gameNumber, username1, score1, gameNumber1
    else:
        want_to_play[gameID] = (username, gameNumber)
        return 8, username, None, gameNumber, None, None, None
