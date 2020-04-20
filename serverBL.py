import sqlite3
import sys

def register(username, password, city, birthYear, mothersName):
    print("register")
    conn = sqlite3.connect('user24.db')
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
    conn = sqlite3.connect('user24.db')
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
    conn = sqlite3.connect('user24.db')
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
    return (ret, password)