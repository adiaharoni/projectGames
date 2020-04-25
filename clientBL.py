from time import sleep
import clientComm

_fe_login_res = None
_fe_register_res = None
_fe_forgot_password_res = None
_callback_dict = {}
_username = ""


def init():
    clientComm.init()


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


def want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, opponentGameNumber):
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
        print("opponentScore:" + opponentScore + "opponentGameNumber: " + opponentGameNumber)
        fe_want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, opponentGameNumber)

