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

def init():
    my_socket.connect(("127.0.0.1", 2223))
    sendThread = Thread(target= client_send, args=(my_socket,))
    sendThread.start()
    recvThread = Thread(target= client_recv, args=(my_socket,))
    recvThread.start()

def register(register_res,username, password, city, birthYear, mothersName):
    global _register_res
    _register_res = register_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(password)).zfill(2) + password+str(len(city)).zfill(2) + city + birthYear+str(len(mothersName)).zfill(2) + mothersName
    str_data = time + str(len(username)).zfill(2) + username + "01" + sender_message
    send_q.put(str_data)

def login(login_res, username, password):
    global _login_res
    _login_res = login_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(password)).zfill(2) + password
    str_data = time + str(len(username)).zfill(2) + username + "02" + sender_message
    send_q.put(str_data)

def forgot_password(forgot_password_res, username, city, birthYear, mothersName):
    global _forgot_password_res
    _forgot_password_res = forgot_password_res
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sender_message = str(len(city)).zfill(2) + city + birthYear+str(len(mothersName)).zfill(2) + mothersName
    str_data = time + str(len(username)).zfill(2) + username + "03"+ sender_message
    send_q.put(str_data)

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
    elif ret1 == 99:
        mesg = "command unknown"
    return mesg
