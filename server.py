import socket
import select
from datetime import datetime
import serverBL

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 2223))
server_socket.listen(5)
open_client_sockets = []
messages_to_send = []
users = {}


def send_waiting_messages(w_list):
    for message in messages_to_send:
        (client_socket, data) = message
        print("message in messages_to_send")
        if client_socket in w_list:
            print("client_socket.send(data)")
            client_socket.send(data)
            messages_to_send.remove(message)


def create_msg(time, user_name, sender_message):
    str_data = time + str(len(user_name)).zfill(2) + user_name + "1" + str(len(sender_message)).zfill(2) + sender_message
    print("sending: " + str_data)
    data = str.encode(str_data)
    return data


def parse_header(data):
    # decode- from bytes to string
    # parse the mesg
    print("receive data:"+receive_data)
    # command
    idx = 0
    command = int(receive_data[idx:idx + 2])
    print("command:"+receive_data[idx:idx + 2])
    idx = idx + 2
    time1 = receive_data[idx:idx+14]
    print("time1:"+time1)
    idx = idx+14
    name_len = int(receive_data[idx:idx + 2])
    print ("name_len:"+receive_data[idx:idx + 2])
    idx = idx + 2
    user_name = receive_data[idx:idx + name_len]
    print("user_name:"+user_name)
    idx = idx + name_len
    sender_msg = receive_data[idx:]
    print("sender_msg:"+sender_msg)
    return time1, user_name, command, sender_msg


def register(time1, user_name, command, sender_msg):
    print(time1 + " register "+ user_name)
    print("password len: " + sender_msg[0:2])
    password_len = int(sender_msg[0:2])
    idx = 2
    password = sender_msg[idx:idx + password_len]
    print("password: " + password)
    idx = idx + password_len
    print("city_len: " + sender_msg[idx:idx + 2])
    city_len = int(sender_msg[idx:idx+2])
    idx = idx+2
    city = sender_msg[idx:idx + city_len]
    print("city:"+city)
    idx = idx + city_len
    birth_year = sender_msg[idx:idx + 4]
    print("birth_year:"+birth_year)
    idx = idx + 4
    print("mother's name len:"+sender_msg[idx:idx+2])
    mothers_name_len = int(sender_msg[idx:idx+2])
    idx = idx+2
    mothers_name = sender_msg[idx:idx + mothers_name_len]
    print("mothers_name:"+mothers_name)
    status_code = serverBL.register(user_name, password, city, birth_year, mothers_name)
    return str(command).zfill(2) + str(status_code).zfill(2)


def login(socket, time1, user_name, command, sender_msg):
    print(time1 + " login " + user_name)
    password_len = int(sender_msg[0:2])
    idx = 2
    password = sender_msg[idx:idx + password_len]
    status_code = serverBL.login(user_name, password)
    if status_code == 0:
        if user_name in users.keys():
            status_code = 16
        else:
            users[user_name] = socket
    return str(command).zfill(2) + str(status_code).zfill(2)


def forgot_password(time1, user_name, command, sender_msg):
    print(time1 + "forgot_password " + user_name)
    city_len = int(sender_msg[0:2])
    idx = 2
    city = sender_msg[idx:idx + city_len]
    idx = idx + city_len
    birth_year = sender_msg[idx:idx + 4]
    idx = idx + 4
    mothers_name_len = int(sender_msg[idx:idx + 2])
    idx = idx + 2
    mothers_name = sender_msg[idx:idx + mothers_name_len]
    (status_code, password) = serverBL.forgot_password(user_name, city, birth_year, mothers_name)
    return str(command).zfill(2)+str(status_code).zfill(2)+str(len(password)).zfill(2)+password


def startGame(user_name, gameId, game_number, score , opponent_user_name, opponent_score, server_game_number):
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    print("user_name: " + user_name + " gameId: " + gameId + " game_number:" + game_number + " score: " + str(score) +
          " opponent_user_name: " + opponent_user_name + " opponent_score:" + str(opponent_score) + "server_game_number:" +server_game_number)
    str_score = str(score)
    sender_message = str(gameId).zfill(2) + str(game_number) + str(len(str_score)).zfill(2) + str_score
    sender_message += str(len(str(opponent_score))).zfill(2) + str(opponent_score) + server_game_number
    str_data = "05" + time + str(len(opponent_user_name)).zfill(2) + opponent_user_name + sender_message
    print("start game:" + str_data)
    messages_to_send.append((users[user_name], str.encode(str_data)))


def want_to_play(time1, user_name, command, sender_msg):
    game_id = sender_msg[0:2]
    game_number = sender_msg[2:]
    print(time1 + " game_id:"+ game_id + " game_number:" + game_number)
    (status_code, user_name, score, game_number, user_name1, score1, game_number1, server_game_number) = serverBL.want_to_play(user_name, game_id, game_number)
    ret = str(command).zfill(2)+str(status_code).zfill(2) + str(game_number)
    if status_code == 9:
        startGame(user_name1, game_id, game_number1, score1, user_name, score, server_game_number)
        ret = ret + str(len(str(score))).zfill(2) + str(score) + str(len(user_name1)).zfill(2) + user_name1 + str(len(str(score1))).zfill(2) + str(score1) + server_game_number
    return ret


def opponent_play_cell(user_name, opponent_user_name, server_game_number, cell, status_code, score, opponent_score):
    print("Server.opponent_play_cell server_game_number:" + server_game_number + " cell:" + str(cell))
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = server_game_number + str(cell).zfill(2) + str(status_code).zfill(2) + str(len(str(score))).zfill(2) + str(score) + str(len(str(opponent_score))).zfill(2) + str(opponent_score)
    str_data = "07" + time + str(len(opponent_user_name)).zfill(2) + opponent_user_name + sender_message
    print("Server.opponent_play_cell sending:" + str_data)
    messages_to_send.append((users[user_name], str.encode(str_data)))


def play_cell(time1, user_name, command, sender_msg):
    server_game_number = sender_msg[0:36]
    cell = sender_msg[36:]
    print(time1 + " Server.play cell server_game_number:" + server_game_number + " cell:" + cell)
    status_code, opponent_user_name, score, score1 = serverBL.play_cell_game(user_name, server_game_number, cell)
    if status_code == "12":
        # tie
        opponent_play_cell(opponent_user_name, user_name, server_game_number, cell, "12", score1, score)
    elif status_code == "13":
        # win
        opponent_play_cell(opponent_user_name, user_name, server_game_number, cell, "14", score1, score)
    else:
        opponent_play_cell(opponent_user_name, user_name, server_game_number, cell, status_code, 0, 0)
    return str(command).zfill(2) + server_game_number + str(status_code).zfill(2) + str(len(str(score))).zfill(2) + str(score) + str(len(str(score1))).zfill(2) + str(score1)


def abort_game(time1, user_name, command, sender_msg):
    print(time1 + " abort game by" + user_name)
    game_id = sender_msg[0:2]
    game_number = sender_msg[2:]
    print(time1 + " game_id:" + game_id + " game_number:" + game_number)
    status_code, opponent_user_name, score, opponent_score = serverBL.abort_game(user_name, game_id, game_number)
    if status_code == "15":
        # abort during game, so opponent wins
        opponent_play_cell(opponent_user_name, user_name, game_number, 0, "15", opponent_score, score)
    return str(command).zfill(2) + game_number + "00"


while (True):
    r_list, w_list, x_list = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in r_list:
        # if new client connection add it to list of client sockets. we will use this in the future
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
            print("open_client_sockets.append(new_socket)")
        else:
            # msg from exiting client
            data = ""
            error = False
            try:
                data = current_socket.recv(1024)
            except:
                error = True
                for socket in open_client_sockets:
                    if socket == current_socket:
                        open_client_sockets.remove(current_socket)
                print("data = current_socket.recv(1024) exception")
            if error is False:
                receive_data = data.decode()
                if receive_data == "":
                    open_client_sockets.remove(current_socket)
                    for user_name, socket in users.items():
                        if socket == current_socket:
                            del users[user_name]
                            break
                    print("Connection with client closed.")
                else:
                    print("received data " + receive_data)
                    (time1, user_name, command, sender_msg) = parse_header(receive_data)
                    ret = 0
                    if command == 1:
                        ret = register(time1, user_name, command, sender_msg)
                    elif command == 2:
                        ret = login(current_socket, time1, user_name, command, sender_msg)
                    elif command == 3:
                        ret = forgot_password(time1, user_name, command, sender_msg)
                    elif command == 4:
                        ret = want_to_play(time1, user_name, command, sender_msg)
                    elif command == 6:
                        ret = play_cell(time1, user_name, command, sender_msg)
                    elif command == 8:
                        ret = abort_game(time1, user_name, command, sender_msg)
                    else:
                        # command unknown
                        ret = str(command).zfill(2) + "99"
                    print("sending: " + ret)
                    data = str.encode(ret)
                    current_socket.send(data)
    send_waiting_messages(w_list)
