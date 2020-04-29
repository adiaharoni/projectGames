import sqlite3
import sys
import uuid

want_to_play = {}
dbName = "AAbox.db"
cell_dict = {}

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

def get_scores(username, username1, gameID):
    query = "SELECT * from GAMES where username in ( '" + username1 + "' ,  '" + username + "' ) and gameID = " + gameID
    print("query = ", query, "\n")
    conn = sqlite3.connect('AAbox.db')
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
    return score, score1

def wantToPlay(username, gameID, gameNumber):
    if gameID in want_to_play.keys():
        (username1, gameNumber1) = want_to_play[gameID]
        score, score1 = get_scores(username, username1, gameID)
        if gameID == "00":
            serverGameNumber= startXO(username1, username)
        else:
            serverGameNumber = start_four_in_a_row(username1, username)
        del want_to_play[gameID]
        return 9, username, score, gameNumber, username1, score1, gameNumber1, serverGameNumber
    else:
        want_to_play[gameID] = (username, gameNumber)
        return 8, username, None, gameNumber, None, None, None, None

def set_Score(result_num, username, gameId):
    conn = sqlite3.connect('AAbox.db')
    cursor = conn.execute(
        "SELECT * from GAMES where username= '" + username + "' and gameId= '" + gameId + "'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not in db!")
        conn.execute("INSERT INTO GAMES (username,gameId, score) \
                                      VALUES ('" + username + "', '" + gameId + "', '" + str(result_num) + "' )")
    else:
        for row in rows:
            print("in cursor")
            score = row[2]
        new_score = score + result_num
        conn.execute("UPDATE GAMES SET score = '" + str(new_score) + "' WHERE username = '" + username + "' and gameId= '" + gameId + "'")
    conn.commit()
    conn.close()
    sys.stdout.flush()

def startXO(usernameX, usernameO):
    serverGameNumber = str(uuid.uuid4())
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    turn = 0
    cell_dict[serverGameNumber] = board, turn, usernameX, usernameO
    print ("usernameX:" + usernameX + " usernameO:"+usernameO)
    return serverGameNumber


def start_four_in_a_row(usernameX, usernameO):
    serverGameNumber = str(uuid.uuid4())
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
    turn = 0
    cell_dict[serverGameNumber] = board, turn, usernameX, usernameO
    print("usernameX:" + usernameX + " usernameO:" + usernameO)
    return serverGameNumber

def play_cell_game(username, serverGameNumber, cell):
    board, turn, usernameX, usernameO = cell_dict[serverGameNumber]
    print("play_cell_game usernameX:" + usernameX + " usernameO:" + usernameO + " cell:"+cell)
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
        if username == usernameX:
            symbol = "X"
        else:
            symbol ="O"
        if checkWinXo(board, symbol) is True:
            print("check win!!!:")
            set_Score(5, username, "00")
            status_code = "13"
            del cell_dict[serverGameNumber]
        elif checkTieXO(board) is True:
            print("check tie!!!:")
            status_code = "12"
            set_Score(2, username, "00")
            set_Score(2, opponentUsername, "00")
            del cell_dict[serverGameNumber]
        else:
            cell_dict[serverGameNumber] = board, turn, usernameX, usernameO
    score = 0
    score1 = 0
    if status_code == "12" or status_code == "13":
        score, score1 = get_scores(username, opponentUsername, "00")
    print("status_code:" + status_code + " opponentUsername:" + opponentUsername)
    return status_code, opponentUsername, score, score1

def checkWinXo(board, symbol):
    print("board: "+board[0] + board[1] + board[2] + board[3] + board[4] + board[5] + board[6] + board[7] + board[8])
    check = True
    row = 0
    col = 0
    #check rows
    while row < 3:
        check = True
        col = 0
        while check is True and col < 3:
            idx = 3 * row + col
            if board[idx] != symbol:
                check = False
            else:
                col= col+1
        if col == 3:
            print( symbol + " wins")
            return True
        else:
            row = row+1
    #check cols
    col = 0
    while col < 3:
        check = True
        row = 0
        while check and row < 3:
            idx = 3 * row + col
            if board[idx] != symbol:
                check = False
            else:
                row= row+1
        if row == 3:
            print( symbol + " wins")
            return True
        else:
            col = col+1
    #check diagonals
    if check_diagonals(board, 3, symbol, 0, 0, 3, 1, 1) is True:
        return True
    if check_diagonals(board, 3, symbol, 0, 2, 3, 1, -1) is True:
        return True

def checkTieXO(board):
    tie = True
    i = 0
    while tie is True and i<9:
        if board[i] == str(i):
            tie = False
        else:
            i = i+1
    return tie


def check_diagonals(board, board_size, symbol, row, col, count, delta_row, delta_col):
    i = 0
    while i < count:
        idx = board_size * row + col
        if board[idx] != symbol:
            return False
        else:
            row = row + delta_row
            col = col + delta_col
            i = i + 1
    print(symbol + " wins")
    return True


def check_win_four_in_a_row(board, symbol):
    print("board: " + board[0] + board[1] + board[2] + board[3] + board[4] + board[5] + board[6] + board[7] + board[8])
    first_equal = True
    check_row = True
    row = 0
    col = 0
    # check rows
    while check_row is True:
        check_col = True
        col = 0
        max_col = 3
        if board[5*row] != symbol:
            col = 1
            max_col = 4
        while check_col is True and col <= max_col:
            idx = 5 * row + col
            if board[idx] != symbol:
                check_col = False
            else:
                col = col + 1
        if col > max_col:
            print(symbol + " wins")
            return True
        else:
            row = row + 1
    # check cols
    check_col = True
    while check_col is True:
        check_row = True
        row = 0
        max_row = 3
        if board[5*col] != symbol:
            col = 1
            max_col = 4
        while check_row is True and col <= max_row:
            idx = 5 * row + col
            if board[idx] != symbol:
                check_col = False
            else:
                row = row + 1
        if col > max_row:
            print(symbol + " wins")
            return True
        else:
            col = col + 1
    # check diagonals
    if check_diagonals(board, 5, symbol, 0, 0, 4, 1, 1) is True:
        return True
    if check_diagonals(board, 5, symbol, 1, 1, 4, 1, 1) is True:
        return True
    if check_diagonals(board, 5, symbol, 1, 0, 4, 1, 1) is True:
        return True
    if check_diagonals(board, 5, symbol, 0, 1, 4, 1, 1) is True:
        return True

    if check_diagonals(board, 5, symbol, 0, 4, 4, 1, -1) is True:
        return True
    if check_diagonals(board, 5, symbol, 1, 3, 4, 1, -1) is True:
        return True
    if check_diagonals(board, 5, symbol, 0, 3, 4, 1, -1) is True:
        return True
    if check_diagonals(board, 5, symbol, 1, 4, 4, 1, -1) is True:
        return True
    return False


def check_tie_four_in_a_row(board):
    tie = True
    i = 0
    while tie is True and i < 25:
        if board[i] == str(i):
            tie = False
        else:
            i = i+1
    return tie
