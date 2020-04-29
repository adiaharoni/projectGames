from time import sleep
import clientComm

_fe_login_res = None
_fe_register_res = None
_fe_forgot_password_res = None
_callback_dict = {}
_username = ""


def init():
    clientComm.init()

def get_user_name():
    return _username

def register(fe_register_res,username, password, city, birthYear, mothersName):
    global _fe_register_res
    _fe_register_res = fe_register_res
    global _username
    _username = username
    clientComm.register(register_res,username, password, city, birthYear, mothersName)


def login(fe_login_res, username, password):
    global _fe_login_res
    _fe_login_res = fe_login_res
    global _username
    _username = username
    clientComm.login(login_res,username, password)


def forgot_password(fe_forgot_password_res, username, city, birthYear, mothersName):
    global _fe_forgot_password_res
    _fe_forgot_password_res = fe_forgot_password_res
    global _username
    _username = username
    clientComm.forgot_password(forgot_password_res, username, city, birthYear, mothersName)


def want_to_play(fe_want_to_play_res, gameId, game_number):
    global _callback_dict
    print(game_number)
    _callback_dict[str(game_number)] = fe_want_to_play_res
    global _username
    clientComm.want_to_play(want_to_play_res, _username, gameId, game_number)

def set_play_XO_callback(fe_XO_play_res, serverGameNumber):
    global _callback_dict
    print(serverGameNumber)
    _callback_dict[serverGameNumber] = fe_XO_play_res
    clientComm.set_play_XO_callback(play_XO_res)


def playXO(fe_XO_play_res, serverGameNumber, cell):
    global _callback_dict
    print(serverGameNumber)
    _callback_dict[serverGameNumber] = fe_XO_play_res
    global _username
    clientComm.play_XO(play_XO_res, _username, serverGameNumber, cell)

def register_res(status_code, status_txt):
    print("BL status_code=" + str(status_code) + " text:" + status_txt)
    global _fe_register_res
    _fe_register_res(status_code, status_txt)


def login_res(status_code, status_txt):
    print("BL status_code=" + str(status_code) + " text:" + status_txt)
    global _fe_login_res
    _fe_login_res(status_code, status_txt)


def forgot_password_res(status_code, status_txt, password):
    if password == 00:
        print("BL status_code=" + str(status_code) + " text:" + status_txt + " password: " + str(password))
    else:
        print("BL status_code=" + str(status_code) + " text:" + status_txt)
    global _fe_forgot_password_res
    _fe_forgot_password_res(status_code, status_txt, password)


def want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, serverGameNumber):
    global _callback_dict
    print("len: "+str(len(_callback_dict.keys())))
    for key in _callback_dict:
        print(key)
    fe_want_to_play_res = _callback_dict[game_number]
    if status_code == "08":
        fe_want_to_play_res(status_code, status_txt, game_number, None, None, None, None)
    else:
        print("BL status_code=" + status_code + " text:" + status_txt)
        print(" game_number:" + game_number + "score:" + score + "opponentUsername:" + opponentUsername)
        print("serverGameNumber:" + opponentScore + "opponentGameNumber: " + serverGameNumber)
        #switch mapping to server game number
        del _callback_dict[game_number]
        _callback_dict[serverGameNumber] = fe_want_to_play_res
        fe_want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, serverGameNumber)


def play_XO_res(serverGameNumber, status_code, status_text, opponent_move, cell, score, opponent_score):
    global _callback_dict
    fe_XO_play_res = _callback_dict[serverGameNumber]
    fe_XO_play_res(status_code, status_text, opponent_move, cell, score, opponent_score)
