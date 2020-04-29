import sys
import clientBL
import uuid


symbol = None
color = None
board = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
         "20", "21", "22", "23", "24"]
buttons = []
turn = 0
_serverGameNumber = None
_page_game_number = None
_opponent_user_name = ""
_abort_game = None
abort_game = True

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def fe_want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, serverGameNumber):
    global w
    print('fe_want_to_play_res')
    sys.stdout.flush()
    opponent_username_Label = w.opponent_username_Label
    opponent_score_Label= w.opponent_score_Label
    user_score_Label= w.user_score_Label
    symbol_Label=w.symbol_Label
    global symbol, turn, color
    if status_code == "08":
        opponent_username_Label.configure(text=status_txt + " (" + status_code + ")")
        symbol = "X"
        color = "red"
        enableButtons(True)
    else:
        global _opponent_user_name
        _opponent_user_name = opponentUsername
        opponent_username_Label.configure(text= "opponent: "+opponentUsername)
        opponent_score_Label.configure(text="opponent score: " + opponentScore)
        user_score_Label.configure(text="my score: " + score)
        if symbol == None:
            symbol = "O"
            color = "yellow"
        symbol_Label.configure(text="you are: " + color)
        w.turn_Label.configure(text="red turn")
        enableButtons(False)
        global _serverGameNumber
        _serverGameNumber = serverGameNumber
        clientBL.set_play_cell_game_callback(fe_four_in_a_row_play_res, _serverGameNumber)

def enableButtons(waiting):
    global w, color
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
        w.Button1.configure(state='disabled', background=color)
    else:
        w.Button1.configure(state='normal')
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
        w.Button2.configure(state='disabled', background=color)
    else:
        w.Button2.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
        w.Button3.configure(state='disabled', background=color)
    else:
        w.Button3.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
        w.Button4.configure(state='disabled', background=color)
    else:
        w.Button4.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or waiting is True:
        w.Button5.configure(state='disabled', background=color)
    else:
        w.Button5.configure(state='normal')

def update_board(cell, symbol):
    global w
    if symbol == "X":
        if cell == 0:
            w.Frame2_000.configure(background="red")
        elif cell == 1:
            w.Frame2_001.configure(background="red")
        elif cell == 2:
            w.Frame2_002.configure(background="red")
        elif cell == 3:
            w.Frame2_003.configure(background="red")
        elif cell == 4:
            w.Frame2_004.configure(background="red")
        elif cell == 5:
            w.Frame2_005.configure(background="red")
        elif cell == 6:
            w.Frame2_006.configure(background="red")
        elif cell == 7:
            w.Frame2_007.configure(background="red")
        elif cell == 8:
            w.Frame2_008.configure(background="red")
        elif cell == 9:
            w.Frame2_009.configure(background="red")
        elif cell == 10:
            w.Frame2_010.configure(background="red")
        elif cell == 11:
            w.Frame2_011.configure(background="red")
        elif cell == 12:
            w.Frame2_012.configure(background="red")
        elif cell == 13:
            w.Frame2_013.configure(background="red")
        elif cell == 14:
            w.Frame2_014.configure(background="red")
        elif cell == 15:
            w.Frame2_015.configure(background="red")
        elif cell == 16:
            w.Frame2_016.configure(background="red")
        elif cell == 17:
            w.Frame2_017.configure(background="red")
        elif cell == 18:
            w.Frame2_018.configure(background="red")
        elif cell == 19:
            w.Frame2_019.configure(background="red")
        elif cell == 20:
            w.Frame2_020.configure(background="red")
        elif cell == 21:
            w.Frame2_021.configure(background="red")
        elif cell == 22:
            w.Frame2_022.configure(background="red")
        elif cell == 23:
            w.Frame2_023.configure(background="red")
        elif cell == 24:
            w.Frame2_024.configure(background="red")
    if symbol == "O":
        if cell == 0:
            w.Frame2_000.configure(background="yellow")
        elif cell == 1:
            w.Frame2_001.configure(background="yellow")
        elif cell == 2:
            w.Frame2_002.configure(background="yellow")
        elif cell == 3:
            w.Frame2_003.configure(background="yellow")
        elif cell == 4:
            w.Frame2_004.configure(background="yellow")
        elif cell == 5:
            w.Frame2_005.configure(background="yellow")
        elif cell == 6:
            w.Frame2_006.configure(background="yellow")
        elif cell == 7:
            w.Frame2_007.configure(background="yellow")
        elif cell == 8:
            w.Frame2_008.configure(background="yellow")
        elif cell == 9:
            w.Frame2_009.configure(background="yellow")
        elif cell == 10:
            w.Frame2_010.configure(background="yellow")
        elif cell == 11:
            w.Frame2_011.configure(background="yellow")
        elif cell == 12:
            w.Frame2_012.configure(background="yellow")
        elif cell == 13:
            w.Frame2_013.configure(background="yellow")
        elif cell == 14:
            w.Frame2_014.configure(background="yellow")
        elif cell == 15:
            w.Frame2_015.configure(background="yellow")
        elif cell == 16:
            w.Frame2_016.configure(background="yellow")
        elif cell == 17:
            w.Frame2_017.configure(background="yellow")
        elif cell == 18:
            w.Frame2_018.configure(background="yellow")
        elif cell == 19:
            w.Frame2_019.configure(background="yellow")
        elif cell == 20:
            w.Frame2_020.configure(background="yellow")
        elif cell == 21:
            w.Frame2_021.configure(background="yellow")
        elif cell == 22:
            w.Frame2_022.configure(background="yellow")
        elif cell == 23:
            w.Frame2_023.configure(background="yellow")
        elif cell == 24:
            w.Frame2_024.configure(background="yellow")

def fe_four_in_a_row_play_res(status_code, status_txt, opponent_move, cell, score, opponent_score):
    print("fe_four_in_a_row_play_res opponent_move:" + str(opponent_move) + " cell:"+str(cell))
    global w
    #this is the opponent move
    if opponent_move == 1:
        if symbol == "X":
            board[cell] = "O"
            update_board(cell, "O")
        else:
            board[cell] = "X"
            update_board(cell, "X")

    if status_code == "00":
        global turn
        if turn == 0:
            turn = 1
            w.turn_Label.configure(text="yellow turn")
        else:
            turn = 0
            w.turn_Label.configure(text="red turn")
        waiting = False
        enableButtons(waiting)
    elif status_code == "12" or status_code == "13" or status_code == "14" or status_code == "15":
        global abort_game
        abort_game = False
        startResultPage(status_code, status_txt, score, opponent_score)
    else:
        opponent_username_Label = w.opponent_username_Label
        opponent_username_Label.configure(text=status_txt)

def set_close_callback(abort_game):
    global _abort_game
    _abort_game = abort_game

def startResultPage(status_code, status_txt, score, opponent_score):
    sys.stdout.flush()
    sys.path.append('..\\resultPage')
    import resultPage
    import resultPage_support
    resultPage.create_Toplevel1(root, 'Hello', top_level)
    global _opponent_user_name
    print ("startResultPage _opponent_user_name:"+_opponent_user_name)
    resultPage_support.set_results(status_code, status_txt, score, _opponent_user_name, opponent_score, game_over)


def button_click(col):
    print("fourInARowPage_support button_click:" + str(col))
    global symbol, w, _serverGameNumber
    finish = False
    row = 0
    cell = 0
    while not finish and row < 5:
        cell = 5*row + col
        if board[cell] == str(cell).zfill(2):
            finish = True
        else:
            row = row+1
    if finish is False:
        opponentName_Label = w.opponentName_Label
        opponentName_Label.configure(text="this row is full")
    else:
        board[cell] = symbol
        update_board(cell, symbol)
    print("fourInARowPage_support click cell:" + str(cell))
    waiting = True
    enableButtons(waiting)
    clientBL.play_cell_game(fe_four_in_a_row_play_res, _serverGameNumber, cell)

def on_close():
    print("fourInARowPage_support on_close")
    global _game_over, _serverGameNumber, _page_game_number, abort_game
    if _game_over is not None:
        if _serverGameNumber == None:
            _game_over("01", _page_game_number, abort_game, False)
        else:
            _game_over("01", _serverGameNumber, abort_game, False)

def game_over(play_again):
    destroy_window()
    global _game_over, _serverGameNumber, abort_game
    if _game_over is not None:
        _game_over("01", _serverGameNumber, abort_game, play_again)

def init(top, gui, *args, **kwargs):
    global w, top_level, root, _page_game_number
    w = gui
    top_level = top
    root = top
    _page_game_number = str(uuid.uuid4())
    clientBL.want_to_play(fe_want_to_play_res, "01", _page_game_number)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import fourInARowPage
    fourInARowPage.vp_start_gui()




