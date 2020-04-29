import sys
import uuid
import clientBL

symbol = None
board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
buttons = []
turn = 0
_serverGameNumber = ""
_page_game_number = None
_opponent_user_name = ""
_abort_game = None

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
    opponentName_Label = w.opponentName_Label
    opponentScore_Label= w.opponentScore_Label
    userScore_Label= w.userScore_Label
    symbol_Label=w.symbol_Label
    global symbol
    global turn
    if status_code == "08":
        opponentName_Label.configure(text=status_txt + " (" + status_code + ")")
        symbol = "X"
        enableButtons(True)
    else:
        global _opponent_user_name
        _opponent_user_name = opponentUsername
        opponentName_Label.configure(text= "opponent: "+opponentUsername)
        opponentScore_Label.configure(text="opponent score: " + opponentScore)
        userScore_Label.configure(text="your score: " + score)
        if symbol == None:
            symbol = "O"
        symbol_Label.configure(text="you are: " + symbol)
        enableButtons(False)
        global _serverGameNumber
        _serverGameNumber = serverGameNumber
        clientBL.set_play_XO_callback(fe_XO_play_res, _serverGameNumber)

def enableButtons(waiting):
    global w
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[0] != "0" or waiting is True:
        w.Button0.configure(state='disabled')
    else:
        w.Button0.configure(state='normal')
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[1] != "1" or waiting is True:
        w.Button1.configure(state='disabled')
    else:
        w.Button1.configure(state='normal')
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[2] != "2" or waiting is True:
        w.Button2.configure(state='disabled')
    else:
        w.Button2.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[3] != "3" or waiting is True:
        w.Button3.configure(state='disabled')
    else:
        w.Button3.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[4] != "4" or waiting is True:
        w.Button4.configure(state='disabled')
    else:
        w.Button4.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[5] != "5" or waiting is True:
        w.Button5.configure(state='disabled')
    else:
        w.Button5.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[6] != "6" or waiting is True:
        w.Button6.configure(state='disabled')
    else:
        w.Button6.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[7] != "7" or waiting is True:
        w.Button7.configure(state='disabled')
    else:
        w.Button7.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[8] != "8" or waiting is True:
        w.Button8.configure(state='disabled')
    else:
        w.Button8.configure(state='normal')


def update_board(cell, symbol):
    global w
    if cell == 0:
        w.Button0.configure(text=symbol)
    elif cell == 1:
        w.Button1.configure(text=symbol)
    elif cell == 2:
        w.Button2.configure(text=symbol)
    elif cell == 3:
        w.Button3.configure(text=symbol)
    elif cell == 4:
        w.Button4.configure(text=symbol)
    elif cell == 5:
        w.Button5.configure(text=symbol)
    elif cell == 6:
        w.Button6.configure(text=symbol)
    elif cell == 7:
        w.Button7.configure(text=symbol)
    elif cell == 8:
        w.Button8.configure(text=symbol)


def fe_XO_play_res(status_code, status_txt, opponent_move, cell, score, opponent_score):
    print("fe_XO_play_res opponent_move:" + str(opponent_move) + " cell:"+str(cell))
    global w
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
        else:
            turn = 0
        waiting = False
        enableButtons(waiting)
    elif status_code == "12" or status_code == "13" or status_code == "14":
        startResultPage(status_code, status_txt, score, opponent_score)
    else:
        opponentName_Label = w.opponentName_Label
        opponentName_Label.configure(text=status_txt)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    clientBL.want_to_play(fe_want_to_play_res, "00", uuid.uuid4())

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
    resultPage_support.set_results(status_code, status_txt, score, _opponent_user_name, opponent_score)


def button_click(cell, button):
    global symbol
    global w
    global _serverGameNumber
    button['text'] = symbol
    waiting = True
    enableButtons(waiting)
    clientBL.playXO(fe_XO_play_res, _serverGameNumber, cell)

def on_close():
    global _abort_game
    if _abort_game is not None:
        _abort_game("00", _serverGameNumber, 1)

def destroy_window():
    # Function which closes the window.

    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import XOPage
    XOPage.vp_start_gui()




