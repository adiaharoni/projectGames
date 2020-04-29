from time import sleep
import clientComm

_fe_login_res = None
_fe_register_res = None
_fe_forgot_password_res = None
_callback_dict = {}
_username = ""


def init():
    return clientComm.init()


def stop():
    clientComm.stop()


def get_user_name():
    return _username


def register(fe_register_res,username, password, city, birth_year, mothers_name):
    global _fe_register_res
    _fe_register_res = fe_register_res
    global _username
    _username = username
    clientComm.register(register_res,username, password, city, birth_year, mothers_name)


def login(fe_login_res, username, password):
    global _fe_login_res
    _fe_login_res = fe_login_res
    global _username
    _username = username
    clientComm.login(login_res,username, password)


def forgot_password(fe_forgot_password_res, username, city, birth_year, mothers_name):
    global _fe_forgot_password_res
    _fe_forgot_password_res = fe_forgot_password_res
    global _username
    _username = username
    clientComm.forgot_password(forgot_password_res, username, city, birth_year, mothers_name)


def want_to_play(fe_want_to_play_res, game_id, game_number):
    global _callback_dict
    print(game_number)
    _callback_dict[str(game_number)] = fe_want_to_play_res
    global _username
    clientComm.want_to_play(want_to_play_res, _username, game_id, game_number)


def set_play_cell_game_callback(fe_play_cell_game_res, server_game_number):
    global _callback_dict
    print(server_game_number)
    _callback_dict[server_game_number] = fe_play_cell_game_res
    clientComm.set_play_cell_game_callback(play_cell_game_res)


def play_cell_game(fe_play_cell_game_res, server_game_number, cell):
    global _callback_dict
    print(server_game_number)
    _callback_dict[server_game_number] = fe_play_cell_game_res
    global _username
    clientComm.play_cell_game(play_cell_game_res, _username, server_game_number, cell)


def abort_game(game_id, game_number):
    clientComm.abort_game(_username, game_id, game_number)


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


def want_to_play_res(status_code, status_txt, game_number, score, opponent_user_name, opponent_score, server_game_number):
    global _callback_dict
    print("len: "+str(len(_callback_dict.keys())))
    for key in _callback_dict:
        print(key)
    fe_want_to_play_res = _callback_dict[game_number]
    if status_code == "08":
        fe_want_to_play_res(status_code, status_txt, game_number, None, None, None, None)
    else:
        print("BL status_code=" + status_code + " text:" + status_txt)
        print(" game_number:" + game_number + "score:" + score + "opponent_user_name:" + opponent_user_name)
        print("server_game_number:" + opponent_score + "opponentGameNumber: " + server_game_number)
        # switch mapping to server game number
        del _callback_dict[game_number]
        _callback_dict[server_game_number] = fe_want_to_play_res
        fe_want_to_play_res(status_code, status_txt, game_number, score, opponent_user_name, opponent_score, server_game_number)


def play_cell_game_res(server_game_number, status_code, status_text, opponent_move, cell, score, opponent_score):
    global _callback_dict
    fe_play_cell_game_res = _callback_dict[server_game_number]
    fe_play_cell_game_res(status_code, status_text, opponent_move, cell, score, opponent_score)
