from socket import *
import select
from datetime import datetime
from threading import *
from time import sleep
from queue import Queue

send_q = Queue()  # מה שהקלינט שולח לסרבר
my_socket = socket()
_login_res = None
_register_res = None
_forgot_password_res = None
_want_to_play_res = None
_play_cell_game_res = None
running = False


def connect_server():
    try:
        my_socket.connect(("127.0.0.1", 2223))
    except:
        print("error connecting to the server")
        return False
    global running
    running = True
    return True


def stop():
    global running
    running = False
    my_socket.close()


def init():
    if connect_server() is False:
        return False
    send_thread = Thread(target=client_send, args=(my_socket,))
    send_thread.start()
    receive_thread = Thread(target=client_receive, args=(my_socket,))
    receive_thread.start()
    print("clientComm init done")
    return True


"""
send messages to server
"""


def create_header(cmd, username): 
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return cmd + time + str(len(username)).zfill(2) + username


def register(register_res, username, password, city, birth_year, mothers_name):
    global _register_res
    _register_res = register_res
    sender_message = str(len(password)).zfill(2) + password+str(len(city)).zfill(2) + city + birth_year+str(len(mothers_name)).zfill(2) + mothers_name
    str_data = create_header("01", username) + sender_message
    send_q.put(str_data)


def login(login_res, username, password):
    global _login_res
    _login_res = login_res
    sender_message = str(len(password)).zfill(2) + password
    str_data = create_header("02", username) + sender_message
    send_q.put(str_data)


def forgot_password(forgot_password_res, username, city, birth_year, mothers_name):
    global _forgot_password_res
    _forgot_password_res = forgot_password_res
    sender_message = str(len(city)).zfill(2) + city + birth_year+str(len(mothers_name)).zfill(2) + mothers_name
    str_data = create_header("03", username) + sender_message
    send_q.put(str_data)


def want_to_play(want_to_play_res, username, game_id, game_number):
    global _want_to_play_res
    _want_to_play_res = want_to_play_res    
    sender_message = str(game_id).zfill(2) + str(game_number)
    str_data = create_header("04", username) + sender_message
    send_q.put(str_data)


def play_cell_game(play_cell_game_res, username, server_game_number, cell):
    global _play_cell_game_res
    _play_cell_game_res = play_cell_game_res
    sender_message = server_game_number + str(cell).zfill(2)
    str_data = create_header("06", username) + sender_message
    send_q.put(str_data)


def set_play_cell_game_callback(play_cell_game_res):
    global _play_cell_game_res
    _play_cell_game_res = play_cell_game_res


def abort_game(username, game_id, game_number):
    sender_message = str(game_id).zfill(2) + str(game_number)
    str_data = create_header("08", username) + sender_message
    send_q.put(str_data)


"""
Parse responses from server
"""


def set_register_res(msg):
    print("comm set_register_res")
    status_code = msg[0:2]
    status_text = get_status_text(status_code)
    global _register_res
    _register_res(status_code, status_text)


def set_login_res(msg):
    print("comm set_login_res")
    status_code = msg[0:2]
    status_text = get_status_text(status_code)
    global _login_res
    _login_res(status_code, status_text)


def set_forgot_password_res(msg):
    status_code = msg[0:2]
    status_text = get_status_text(status_code)
    password_len = msg[2:4]
    password = msg[4:4+int(password_len)]
    global _forgot_password_res
    _forgot_password_res(status_code, status_text, password)


def set_want_to_play_res(msg):
    print("comm set_want_to_play_res ")
    status_code = msg[0:2]
    status_txt = get_status_text(status_code)
    game_number = msg[2:38]
    idx = 38
    print("status_code: "+status_code+" game_number: "+game_number)
    global _want_to_play_res
    if status_code == "08":
        _want_to_play_res(status_code, status_txt, game_number, None, None, None, None)
    else:
        score_len = int(msg[idx:idx+2])
        idx = idx+2
        score = msg[idx:idx+score_len]
        idx = idx+score_len
        opponent_user_name_len = int(msg[idx:idx+2])
        idx = idx+2
        opponent_user_name = msg[idx:idx+opponent_user_name_len]
        idx = idx+opponent_user_name_len
        opponent_score_len = int(msg[idx:idx+2])
        idx = idx+2
        opponent_score = msg[idx:idx+opponent_score_len]
        idx = idx+opponent_score_len
        server_game_number = msg[idx:]
        _want_to_play_res(status_code, status_txt, game_number, score, opponent_user_name, opponent_score, server_game_number)


def parse_scores(msg):
    idx = 0
    score_len = int(msg[idx:idx + 2])
    idx = idx + 2
    score = msg[idx:idx + score_len]
    idx = idx + score_len
    opponent_score_len = int(msg[idx:idx + 2])
    idx = idx + 2
    opponent_score = msg[idx:idx + opponent_score_len]
    idx = idx + opponent_score_len
    return idx, score, opponent_score


def set_start_game(msg):
    idx = 0
    time1 = msg[idx:idx + 14]
    print("time1:" + time1)
    idx = idx + 14
    opponent_name_len = int(msg[idx:idx + 2])
    print("opponent_name_len:" + msg[idx:idx + 2])
    idx = idx + 2
    opponent_user_name = msg[idx:idx + opponent_name_len]
    print("username:" + opponent_user_name)
    idx = idx + opponent_name_len
    game_id = msg[idx:idx+2]
    idx = idx+2
    game_number = msg[idx:idx+36]
    idx = idx+36
    parse_idx, score, opponent_score = parse_scores(msg[idx:])
    idx = idx + parse_idx
    server_game_number = msg[idx:]
    global _want_to_play_res
    _want_to_play_res("09", get_status_text("09"), game_number, score, opponent_user_name, opponent_score, server_game_number)


def set_play_cell_game_res(msg):
    server_game_number = msg[0:36]
    status_code = msg[36:38]
    status_text = get_status_text(status_code)
    parse_idx, score, opponent_score = parse_scores(msg[38:])
    global _play_cell_game_res
    _play_cell_game_res(server_game_number, status_code, status_text, 0, None, score, opponent_score)


def set_opponent_play_cell_game(msg):
    idx = 0
    time1 = msg[idx:idx + 14]
    print("time1:" + time1)
    idx = idx + 14
    opponent_name_len = int(msg[idx:idx + 2])
    print("opponent_name_len:" + msg[idx:idx + 2])
    idx = idx + 2
    opponent_user_name = msg[idx:idx + opponent_name_len]
    print("username:" + opponent_user_name)
    idx = idx + opponent_name_len
    server_game_number = msg[idx:idx + 36]
    idx = idx + 36
    cell = int(msg[idx:idx + 2])
    idx = idx + 2
    status_code = msg[idx:idx + 2]
    idx = idx + 2
    status_text = get_status_text(status_code)
    parse_idx, score, opponent_score = parse_scores(msg[idx:])
    global _play_cell_game_res
    _play_cell_game_res(server_game_number, status_code, status_text, 1, cell, score, opponent_score)


def set_abort_game_res(msg):
    game_number = msg[0:36]
    status_code = msg[36:38]
    print("set_abort_game_res game_number:" + game_number + " status_code: " + status_code)


"""
get messages from server
"""


def client_receive(my_socket):
    global running
    print("start client_receive")

    while running:
        r_list, w_list, x_list = select.select([my_socket], [], [])
        for my_socket in r_list:
            if not running:
                return
            print("my_socket in r_list")
            receive_data = my_socket.recv(1024)
            if receive_data == "":
                print("server close this socket")
                my_socket.close()
                break
                """get out from thread"""
            receive_data = receive_data.decode()
            print("client_receive:" + receive_data)
            cmd_id = int(receive_data[0:2])
            msg = receive_data[2:]
            if cmd_id == 1:
                set_register_res(msg)
            elif cmd_id == 2:
                set_login_res(msg)
            elif cmd_id == 3:
                set_forgot_password_res(msg)
            elif cmd_id == 4:
                set_want_to_play_res(msg)
            elif cmd_id == 5:
                set_start_game(msg)
            elif cmd_id == 6:
                set_play_cell_game_res(msg)
            elif cmd_id == 7:
                set_opponent_play_cell_game(msg)
            elif cmd_id == 8:
                set_abort_game_res(msg)
            else:
                print("command unknown:" + receive_data)


"""
send messages to server
"""


def client_send(my_socket):
    global running
    while running:
        if not send_q.empty():
            data = send_q.get()
            print("client_send:" + data)
            print("3333", current_thread().name)
            my_socket.sendall(data.encode('latin-1'))
        sleep(0.05)  # sleep a little before check the queue again


def get_status_text(ret):
    ret1 = int(ret)
    msg = ""
    if ret1 == 0:
        msg = "ok"
    elif ret1 == 1:
        msg = "error: Username already exists"
    elif ret1 == 2:
        msg = "error: password length < 4"
    elif ret1 == 3:
        msg = "error: empty city"
    elif ret1 == 4:
        msg = "error: year in valid"
    elif ret1 == 5:
        msg = "error: empty mother's name"
    elif ret1 == 6:
        msg = "error: wrong username or password"
    elif ret1 == 7:
        msg = "error: user not found"
    elif ret1 == 8:
        msg = "waiting"
    elif ret1 == 9:
        msg = "game starting"
    elif ret1 == 10:
        msg = "cell not valid"
    elif ret1 == 11:
        msg = "it is not your turn"
    elif ret1 == 12:
        msg = "it's a tie!"
    elif ret1 == 13:
        msg = "you win!!!"
    elif ret1 == 14:
        msg = "you lose"
    elif ret1 == 15:
        msg = "abort during game"
    elif ret1 == 16:
        msg = "this user have already logged in"
    elif ret1 == 99:
        msg = "command unknown"
    return msg
