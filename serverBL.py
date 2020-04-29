import sqlite3
import sys
import uuid

want_to_play1 = {}
dbName = "AAbox.db"
cell_dict = {}


def register(username, password, city, birth_year, mothers_name):
    print("register")
    conn = sqlite3.connect(dbName)
    cursor = conn.execute("SELECT * from users where username= '" + username + "' ")
    rows = cursor.fetchall()
    if len(rows) != 0:
        return 1
        # error: Username already exists
    if len(password) < 4:
        return 2
        # error: password length <4
    elif city == "":
        return 3
        # error: empty city
    elif not birth_year.isdigit():
        return 4
        # error: year in valid
    elif int(birth_year) < 1900 or int(birth_year) > 2020:
        # the year should be between 1900-2020
        return 4
        # error: year in valid
    elif mothers_name == "":
        return 5
        # error: empty mother name"""
    else:
        cursor = conn.execute("INSERT INTO USERS (username,password,city,birth_year,mothers_name) \
                                            VALUES ('" + username + "', '" + password + "', '" + city + "', '" + birth_year + "', '" + mothers_name + "' )")
        conn.commit()
        conn.close()
        sys.stdout.flush()
        return 0
        # ok


def login(username, password):
    print("login")
    conn = sqlite3.connect(dbName)
    cursor = conn.execute(
        "SELECT * from USERS where username= '" + username + "' and password= '" + password + "'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not in db! " + username+" should re-register")
        return 6
        # error: wrong username or password
    else:
        print(username+" is in db!")
        return 0
        # ok
    conn.close()
    sys.stdout.flush()
    return ret


def forgot_password(username, city, birth_year, mothers_name):
    print("forgot_password")
    query = "SELECT * from USERS where username= '" + username + "' and city= '" + city + "' and birth_year= '" + birth_year + "' and mothers_name= '" + mothers_name + "'"
    print("query = ", query, "\n")
    conn = sqlite3.connect('AAbox.db')
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    password = ""
    ret = 0
    if len(rows) == 0:
        print("not in db! you should re-register")
        ret = 7
        """error: user not found"""
    else:
        print("read password")
        for row in rows:
            print("in cursor")
            password = row[1]
            print("password = ", password, "\n")
            ret = 0
            # ok
    conn.commit()
    conn.close()
    sys.stdout.flush()
    return ret, password


def get_scores(username, username1, game_id):
    query = "SELECT * from GAMES where username in ( '" + username1 + "' ,  '" + username + "' ) and game_id = " + game_id
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


def want_to_play(username, game_id, game_number):
    if game_id in want_to_play1.keys():
        (username1, game_number1) = want_to_play1[game_id]
        score, score1 = get_scores(username, username1, game_id)
        if game_id == "00":
            server_game_number = start_xo(username1, username)
        else:
            server_game_number = start_four_in_a_row(username1, username)
        del want_to_play1[game_id]
        return 9, username, score, game_number, username1, score1, game_number1, server_game_number
    else:
        want_to_play1[game_id] = (username, game_number)
        return 8, username, None, game_number, None, None, None, None


def set_score(result_num, username, game_id):
    conn = sqlite3.connect('AAbox.db')
    cursor = conn.execute(
        "SELECT * from GAMES where username= '" + username + "' and game_id= '" + game_id + "'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not in db!")
        conn.execute("INSERT INTO GAMES (username,game_id, score) \
                                      VALUES ('" + username + "', '" + game_id + "', '" + str(result_num) + "' )")
    else:
        for row in rows:
            print("in cursor")
            score = row[2]
        new_score = score + result_num
        conn.execute("UPDATE GAMES SET score = '" + str(new_score) + "' WHERE username = '" + username + 
                     "' and game_id= '" + game_id + "'")
    conn.commit()
    conn.close()
    sys.stdout.flush()


def start_xo(user_name_x, user_name_o):
    server_game_number = str(uuid.uuid4())
    board = ["00", "01", "02", "03", "04", "05", "06", "07", "08"]
    turn = 0
    cell_dict[server_game_number] = board, turn, user_name_x, user_name_o, "00"
    print("user_name_x:" + user_name_x + " user_name_o:"+user_name_o)
    return server_game_number


def start_four_in_a_row(user_name_x, user_name_o):
    server_game_number = str(uuid.uuid4())
    board = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
    turn = 0
    cell_dict[server_game_number] = board, turn, user_name_x, user_name_o, "01"
    print("user_name_x:" + user_name_x + " user_name_o:" + user_name_o)
    return server_game_number


def play_cell_game(username, server_game_number, cell):
    board, turn, user_name_x, user_name_o, game_id = cell_dict[server_game_number]
    print("play_cell_game user_name_x:" + user_name_x + " user_name_o:" + user_name_o + " cell:"+cell)
    status_code = "00"
    opponent_user_name = None
    # set cell
    if username == user_name_x and turn == 0:
        opponent_user_name = user_name_o
        if board[int(cell)] == cell:
            board[int(cell)] = "X"
            turn = 1
            print("X status_code:" + status_code)
        else:
            status_code = "10"
    elif username == user_name_o and turn == 1:
        opponent_user_name = user_name_x
        if board[int(cell)] == cell:
            board[int(cell)] = "O"
            turn = 0
            print("O status_code:" + status_code)
        else:
            status_code = "10"
    else:
        status_code = "11"
    # place cell ok. check result
    if status_code == "00":
        if username == user_name_x:
            symbol = "X"
        else:
            symbol = "O"
        check_win = None
        check_tie = None
        if game_id == "00":
            check_win = check_win_xo
            check_tie = check_tie_xo
        else:
            check_win = check_win_four_in_a_row
            check_tie = check_tie_four_in_a_row
        if check_win(board, symbol) is True:
            print("check win!!!:")
            set_score(5, username, game_id)
            status_code = "13"
            del cell_dict[server_game_number]
        elif check_tie(board) is True:
            print("check tie!!!:")
            status_code = "12"
            set_score(2, username, game_id)
            set_score(2, opponent_user_name, game_id)
            del cell_dict[server_game_number]
        else:
            cell_dict[server_game_number] = board, turn, user_name_x, user_name_o, game_id

    score = 0
    score1 = 0
    if status_code == "12" or status_code == "13":
        if game_id == "00":
            score, score1 = get_scores(username, opponent_user_name, "00")
        else:
            score, score1 = get_scores(username, opponent_user_name, "01")
    print("status_code:" + status_code + " opponent_user_name:" + opponent_user_name)
    return status_code, opponent_user_name, score, score1


def check_win_xo(board, symbol):
    print("board: "+board[0] + board[1] + board[2] + board[3] + board[4] + board[5] + board[6] + board[7] + board[8])
    check = True
    row = 0
    col = 0
    # check rows
    while row < 3:
        check = True
        col = 0
        while check is True and col < 3:
            idx = 3 * row + col
            if board[idx] != symbol:
                check = False
            else:
                col = col+1
        if col == 3:
            print(symbol + " wins")
            return True
        else:
            row = row+1
    # check cols
    col = 0
    while col < 3:
        check = True
        row = 0
        while check and row < 3:
            idx = 3 * row + col
            if board[idx] != symbol:
                check = False
            else:
                row = row+1
        if row == 3:
            print(symbol + " wins")
            return True
        else:
            col = col+1
    # check diagonals
    if check_diagonals(board, 3, symbol, 0, 0, 3, 1, 1) is True:
        return True
    if check_diagonals(board, 3, symbol, 0, 2, 3, 1, -1) is True:
        return True


def check_tie_xo(board):
    tie = True
    i = 0
    while tie is True and i < 9:
        if board[i] == str(i).zfill(2):
            tie = False
        else:
            i = i+1
    return tie


def check_diagonals(board, board_size, symbol, row, col, count, delta_row, delta_col):
    # print("check_diagonals "board_size, symbol, row, col, count, delta_row, delta_col)
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


def four_in_a_row(board, symbol):
    print("four_in_a_row")
    check_row = True
    row = 0
    # check rows
    while check_row is True and row < 5:
        check_col = True
        col = 0
        max_col = 3
        # if the first cell is not symbol, search the cells starting the second one, still may have 4
        if board[5*row] != symbol:
            col = 1
            max_col = 4
        # look in cols of this row
        while check_col is True and col <= max_col:
            print("check " + str(row) + "," + str(col))
            idx = 5 * row + col
            if board[idx] != symbol:
                check_col = False
            else:
                col = col + 1
        if col > max_col:
            print(symbol + " wins")
            return True
        row = row + 1
    return False


def four_in_a_col(board, symbol):
    print("four_in_a_col")
    col = 0
    check_col = True
    while check_col is True and col < 5:
        check_row = True
        row = 0
        max_row = 3
        if board[col] != symbol:
            row = 1
            max_row = 4
        while check_row is True and row <= max_row:
            print("check " + str(row) + "," + str(col))
            idx = 5 * row + col
            if board[idx] != symbol:
                check_row = False
            else:
                row = row + 1
        if row > max_row:
            print(symbol + " wins")
            return True
        col = col + 1
    return False


def check_win_four_in_a_row(board, symbol):
    print("board: " + str(board))
    # check rows
    if four_in_a_row(board, symbol):
        return True
    # check cols
    if four_in_a_col(board, symbol):
        return True
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
    print("no winner")
    return False


def check_tie_four_in_a_row(board):
    tie = True
    i = 0
    while tie is True and i < 25:
        if board[i] == str(i).zfill(2):
            tie = False
        else:
            i = i+1
    return tie


def abort_game(username, game_id, game_number):
    # check if still waiting
    print("serverBL " + username + " abort_game " + game_id)
    if game_id in want_to_play1.keys():
        del want_to_play1[game_id]
        print("serverBL abort_game " + username + " abort_game " + game_id + " abort while waiting")
        return "00", None, None, None
    # abort in the middle
    print("serverBL " + username + " abort_game " + game_id + " in the middle")
    if game_number in cell_dict.keys():
        board, turn, user_name_x, user_name_o, game_id = cell_dict[game_number]
        del cell_dict[game_number]
        opponent_user_name = user_name_x
        if username == user_name_x:
            opponent_user_name = user_name_o
        # opponent wins
        set_score(15, opponent_user_name, game_id)
        score, score1 = get_scores(username, opponent_user_name, game_id)
        return "15", opponent_user_name, score, score1
    # cant find game to abort
    print("serverBL abort_game " + username + " abort_game " + game_id + " cant find game to abort")
    return "00", None, None, None

