import sqlite3
import sys
import uuid

want_to_play = {}
dbName = "AAbox.db"
XOdict = {}

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
    conn = sqlite3.connect('AAbox.db')
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
        serverGameNumber= startXO(username1, username)
        del want_to_play[gameID]
        return 9, username, score, gameNumber, username1, score1, gameNumber1, serverGameNumber
    else:
        want_to_play[gameID] = (username, gameNumber)
        return 8, username, None, gameNumber, None, None, None, None

def startXO(usernameX, usernameO):
    serverGameNumber = str(uuid.uuid4())
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    turn = 0
    XOdict[serverGameNumber] = board, turn, usernameX, usernameO
    print ("usernameX:" + usernameX + " usernameO:"+usernameO)
    return serverGameNumber

def playXO(username, serverGameNumber, cell):
    board, turn, usernameX, usernameO = XOdict[serverGameNumber]
    print("playXO usernameX:" + usernameX + " usernameO:" + usernameO + " cell:"+cell)
    status_code = "00"
    opponentUsername = None
    if username == usernameX and turn == 0:
        opponentUsername = usernameO
        if board[int(cell)] == cell:
            board[int(cell)] = "X"
            turn = 1
            print("X status_code:" + status_code)
        else:
            status_code = "10"
    elif username == usernameO and turn == 1:
        opponentUsername = usernameX
        if board[int(cell)] == cell:
            board[int(cell)] = "O"
            turn = 0
            print("O status_code:" + status_code)
        else:
            status_code = "10"
    else:
        status_code = "11"
    if status_code == "00":
        if checkWinXo(board) is True:
            print("check win!!!:")
            status_code = "13"
            del XOdict[serverGameNumber]
        elif checkTie(board) is True:
            print("check tie!!!:")
            status_code = "12"
            del XOdict[serverGameNumber]
        else:
            XOdict[serverGameNumber] = board, turn, usernameX, usernameO
    print("status_code:" + status_code + " opponentUsername:" + opponentUsername)
    return status_code, opponentUsername

def checkWinXo(board):
    print("board: "+board[0] + board[1] + board[2] + board[3] + board[4] + board[5] + board[6] + board[7] + board[8])
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False

def checkTie(board):
    if board[0] != "0" and board[1] != "1" and board[2] != "2" and board[3] != "3" and board[4] != "4" and board[5] != "5" and board[6] != "6" and board[7] != "7" and board[8] != "8" and checkWinXo(board) is not True:
        return True
    else:
        return False
