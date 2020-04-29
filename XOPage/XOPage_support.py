import sys
import uuid
import clientBL

symbol = None
board = ["00", "01", "02", "03", "04", "05", "06", "07", "08"]
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
        w.turn_Label.configure(text="X turn")
        enableButtons(False)
        global _serverGameNumber
        _serverGameNumber = serverGameNumber
        clientBL.set_play_cell_game_callback(fe_XO_play_res, _serverGameNumber)

def enableButtons(waiting):
    global w
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[0] != "00" or waiting is True:
        w.Button0.configure(state='disabled')
    else:
        w.Button0.configure(state='normal')
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[1] != "01" or waiting is True:
        w.Button1.configure(state='disabled')
    else:
        w.Button1.configure(state='normal')
    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[2] != "02" or waiting is True:
        w.Button2.configure(state='disabled')
    else:
        w.Button2.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[3] != "03" or waiting is True:
        w.Button3.configure(state='disabled')
    else:
        w.Button3.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[4] != "04" or waiting is True:
        w.Button4.configure(state='disabled')
    else:
        w.Button4.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[5] != "05" or waiting is True:
        w.Button5.configure(state='disabled')
    else:
        w.Button5.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[6] != "06" or waiting is True:
        w.Button6.configure(state='disabled')
    else:
        w.Button6.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[7] != "07" or waiting is True:
        w.Button7.configure(state='disabled')
    else:
        w.Button7.configure(state='normal')

    if turn == 0 and symbol == "O" or turn == 1 and symbol == "X" or board[8] != "08" or waiting is True:
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
            w.turn_Label.configure(text="O turn")
        else:
            turn = 0
            w.turn_Label.configure(text="X turn")
        waiting = False
        enableButtons(waiting)
    elif status_code == "12" or status_code == "13" or status_code == "14" or status_code == "15":
        global abort_game
        abort_game = False
        startResultPage(status_code, status_txt, score, opponent_score)
    else:
        opponentName_Label = w.opponentName_Label
        opponentName_Label.configure(text=status_txt)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    start_game()

def start_game():
    global _page_game_number
    _page_game_number = str(uuid.uuid4())
    clientBL.want_to_play(fe_want_to_play_res, "00", _page_game_number)

def set_close_callback(game_over):
    global _game_over
    _game_over = game_over

def startResultPage(status_code, status_txt, score, opponent_score):
    sys.stdout.flush()
    sys.path.append('..\\resultPage')
    import resultPage
    import resultPage_support
    resultPage.create_Toplevel1(root, 'Hello', top_level)
    global _opponent_user_name
    print ("startResultPage _opponent_user_name:"+_opponent_user_name)
    resultPage_support.set_results(status_code, status_txt, score, _opponent_user_name, opponent_score, game_over)


def button_click(cell, button):
    global symbol
    global w
    global _serverGameNumber
    button['text'] = symbol
    board[cell] = symbol
    waiting = True
    enableButtons(waiting)
    clientBL.play_cell_game(fe_XO_play_res, _serverGameNumber, cell)

def on_close():
    print("XOPage_support on_close")
    global _game_over, _serverGameNumber, _page_game_number, abort_game
    if _game_over is not None:
        if _serverGameNumber == None:
            _game_over("00", _page_game_number, abort_game, False)
        else:
            _game_over("00", _serverGameNumber, abort_game, False)

def game_over(play_again):
    destroy_window()
    global _game_over, _serverGameNumber, abort_game
    if _game_over is not None:
        _game_over("00", _serverGameNumber, abort_game, play_again)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import XOPage
    XOPage.vp_start_gui()




