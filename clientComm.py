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
_play_XO_res = None

def connect_server():
    try:
        my_socket.connect(("127.0.0.1", 2223))
    except:
        print("error connecting to the server")
        return False
    return True

def init():
    if connect_server() is not True:
		#TODO return false?
        return
    sendThread = Thread(target= client_send, args=(my_socket,))
    sendThread.start()
    recvThread = Thread(target= client_recv, args=(my_socket,))
    recvThread.start()

def register(register_res,username, password, city, birthYear, mothersName):
    global _register_res
    _register_res = register_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(password)).zfill(2) + password+str(len(city)).zfill(2) + city + birthYear+str(len(mothersName)).zfill(2) + mothersName
    str_data = "01" + time + str(len(username)).zfill(2) + username + sender_message
    send_q.put(str_data)

def login(login_res, username, password):
    global _login_res
    _login_res = login_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(password)).zfill(2) + password
    str_data = "02" + time + str(len(username)).zfill(2) + username + sender_message
    send_q.put(str_data)

def forgot_password(forgot_password_res, username, city, birthYear, mothersName):
    global _forgot_password_res
    _forgot_password_res = forgot_password_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(city)).zfill(2) + city + birthYear+str(len(mothersName)).zfill(2) + mothersName
    str_data = "03" + time + str(len(username)).zfill(2) + username + sender_message
    send_q.put(str_data)

def want_to_play(want_to_play_res, username, gameId, game_number):
    global _want_to_play_res
    _want_to_play_res = want_to_play_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(gameId).zfill(2) + str(game_number)
    str_data = "04" + time + str(len(username)).zfill(2) + username + sender_message
    send_q.put(str_data)

def play_XO(play_XO_res, username, serverGameNumber, cell):
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    global _play_XO_res
    _play_XO_res = play_XO_res
    sender_message = serverGameNumber + str(cell)
    str_data = "06" + time + str(len(username)).zfill(2) + username + sender_message
    send_q.put(str_data)

def set_play_XO_callback(play_XO_res):
    global _play_XO_res
    _play_XO_res = play_XO_res

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
    passwordlen= msg[2:4]
    password = msg[4:4+int(passwordlen)]
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
        scoreLen = int(msg[idx:idx+2])
        idx = idx+2
        score = msg[idx:idx+scoreLen]
        idx = idx+scoreLen
        opponentUsernameLen = int(msg[idx:idx+2])
        idx = idx+2
        opponentUsername = msg[idx:idx+opponentUsernameLen]
        idx = idx+opponentUsernameLen
        opponentScoreLen = int(msg[idx:idx+2])
        idx = idx+2
        opponentScore = msg[idx:idx+opponentScoreLen]
        idx = idx+opponentScoreLen
        serverGameNumber = msg[idx:]
        _want_to_play_res(status_code, status_txt, game_number, score, opponentUsername, opponentScore, serverGameNumber)

def parse_scores(msg):
    idx = 0
    scoreLen = int(msg[idx:idx + 2])
    idx = idx + 2
    score = msg[idx:idx + scoreLen]
    idx = idx + scoreLen
    opponentScoreLen = int(msg[idx:idx + 2])
    idx = idx + 2
    opponentScore = msg[idx:idx + opponentScoreLen]
    idx = idx + opponentScoreLen
    return idx, score, opponentScore

def set_start_game(msg):
    idx = 0
    time1 = msg[idx:idx + 14]
    print("time1:" + time1)
    idx = idx + 14
    opponentNamelen = int(msg[idx:idx + 2])
    print("opponentNamelen:" + msg[idx:idx + 2])
    idx = idx + 2
    opponentUsername = msg[idx:idx + opponentNamelen]
    print("username:" + opponentUsername)
    idx = idx + opponentNamelen
    gameID = msg[idx:idx+2]
    idx = idx+2
    game_number = msg[idx:idx+36]
    idx = idx+36
    parse_idx, score, opponent_score = parse_scores(msg[idx:])
    idx = idx + parse_idx
    serverGameNumber = msg[idx:]
    global _want_to_play_res
    _want_to_play_res("09", get_status_text("09"), game_number, score, opponentUsername, opponent_score, serverGameNumber)


def set_play_XO_res(msg):
    serverGameNumber = msg[0:36]
    status_code = msg[36:38]
    status_text = get_status_text(status_code)
    parse_idx, score, opponent_score = parse_scores(msg[38:])
    global _play_XO_res
    _play_XO_res(serverGameNumber, status_code, status_text, 0, None, score, opponent_score)


def set_opponent_play_XO(msg):
    idx = 0
    time1 = msg[idx:idx + 14]
    print("time1:" + time1)
    idx = idx + 14
    opponentNamelen = int(msg[idx:idx + 2])
    print("opponentNamelen:" + msg[idx:idx + 2])
    idx = idx + 2
    opponentUsername = msg[idx:idx + opponentNamelen]
    print("username:" + opponentUsername)
    idx = idx + opponentNamelen
    serverGameNumber = msg[idx:idx + 36]
    idx = idx + 36
    cell = int(msg[idx:idx + 1])
    idx = idx + 1
    status_code = msg[idx:idx + 2]
    idx = idx + 2
    status_text = get_status_text(status_code)
    parse_idx, score, opponent_score = parse_scores(msg[idx:])
    global _play_XO_res
    _play_XO_res(serverGameNumber, status_code, status_text, 1, cell, score, opponent_score)


#get messages from server
def client_recv(my_socket):
    print("start client_recv")
    while True:
        rlist, wlist, xlist = select.select([my_socket], [], [])
        for my_socket in rlist:
            print("my_socket in rlist")
            recvdata = my_socket.recv(1024)
            if recvdata == "":
                print("server close this socket")
                my_socket.close()
                break #get out from thread
            recvdata = recvdata.decode()
            print ("client_recv:" + recvdata)
            cmdID = int(recvdata[0:2])
            msg = recvdata[2:]
            if cmdID == 1:
                set_register_res(msg)
            elif cmdID == 2:
                set_login_res(msg)
            elif cmdID == 3:
                set_forgot_password_res(msg)
            elif cmdID == 4:
                set_want_to_play_res(msg)
            elif cmdID == 5:
                set_start_game(msg)
            elif cmdID == 6:
                set_play_XO_res(msg)
            elif cmdID == 7:
                set_opponent_play_XO(msg)
            else:
                print("command unknown:" + recvdata)

#send messages from server
def client_send(my_socket):
    while True:
        if send_q.empty() == False:
            data = send_q.get()
            print("client_send:" + data)
            print("3333", current_thread().name)
            my_socket.sendall(data.encode('latin-1'))
        sleep(0.05)  # sleep a little before check the queue again

def get_status_text(ret):
    ret1 = int(ret)
    mesg = ""
    if ret1 == 0:
        mesg = "ok"
    elif ret1 == 1:
        mesg = "error: Username already exists"
    elif ret1 == 2:
        mesg = "error: password length < 4"
    elif ret1 == 3:
        mesg = "error: empty city"
    elif ret1 == 4:
        mesg = "error: year in valid"
    elif ret1 == 5:
        mesg = "error: empty mother's name"
    elif ret1 == 6:
        mesg = "error: wrong username or password"
    elif ret1 == 7:
        mesg = "error: user not found"
    elif ret1 == 8:
        mesg = "waiting"
    elif ret1 == 9:
        mesg = "game starting"
    elif ret1 == 10:
        mesg = "cell not valid"
    elif ret1 == 11:
        mesg = "it is not your turn"
    elif ret1 == 12:
        mesg = "it's a tie!"
    elif ret1 == 13:
        mesg = "you win!!!"
    elif ret1 == 14:
        mesg = "you lose"
    elif ret1 == 99:
        mesg = "command unknown"
    return mesg
