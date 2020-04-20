import socket
import select
from datetime import datetime
import serverBL

server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 2223))
server_socket.listen(5)
open_client_sockets = []
users = {}
messages_to_send = []

def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket, data) = message
        print ("message in messages_to_send")
        if client_socket in wlist:
            print("client_socket.send(data)")
            client_socket.send(data)
            messages_to_send.remove(message)


def create_mesg(time, username, sender_message):
    str_data = time + str(len(username)).zfill(2) + username + "1" + str(len(sender_message)).zfill(2) + sender_message
    print ("sending: " + str_data)
    data = str.encode(str_data)
    return data

def parse_header(data):
    # decode- from bytes to string
    # parse the mesg
    recvdata = data.decode()
    print("recvdata:"+recvdata)
    time1 = recvdata[0:14]
    print("time1:"+time1)
    idx = 14
    namelen = int(recvdata[idx:idx + 2])
    print ("namelen:"+recvdata[idx:idx + 2])
    idx = idx + 2
    username = recvdata[idx:idx + namelen]
    print("username:"+username)
    idx = idx + namelen
    # command
    command = int(recvdata[idx:idx + 2])
    print("command:"+recvdata[idx:idx + 2])
    idx = idx + 2
    sender_msg = recvdata[idx:]
    print("sender_msg:"+sender_msg)
    return (time1, username, command, sender_msg)

def register(time1, username, command, sender_msg):
    print("sender_msg:"+sender_msg)
    print("passwordlen: " + sender_msg[0:2])
    passwordlen = int(sender_msg[0:2])
    idx = 2
    password = sender_msg[idx:idx + passwordlen]
    print("password: " + password)
    idx = idx + passwordlen
    print("citylen: " + sender_msg[idx:idx + 2])
    citylen = int(sender_msg[idx:idx+2])
    idx = idx+2
    city = sender_msg[idx:idx + citylen]
    print("city:"+city)
    idx = idx + citylen
    birthYear = sender_msg[idx:idx + 4]
    print("birthYear:"+birthYear)
    idx = idx + 4
    print ("mothersNamelen:"+sender_msg[idx:idx+2])
    mothersNamelen = int(sender_msg[idx:idx+2])
    idx = idx+2
    mothersName = sender_msg[idx:idx + mothersNamelen]
    print("mothersName:"+mothersName)
    statusCode = serverBL.register(username, password, city, birthYear, mothersName)
    return str(command).zfill(2) + str(statusCode).zfill(2)

def login(time1, username, command, sender_msg):
    passwordlen = int(sender_msg[0:2])
    idx = 2
    password = sender_msg[idx:idx + passwordlen]
    statusCode = serverBL.login(username, password)
    return str(command).zfill(2) + str(statusCode).zfill(2)

def forgotPassword(time1, username, command, sender_msg):
    citylen = int(sender_msg[0:2])
    idx = 2
    city = sender_msg[idx:idx + citylen]
    idx = idx + citylen
    birthYear = sender_msg[idx:idx + 4]
    idx = idx + 4
    mothersNamelen = int(sender_msg[idx:idx + 2])
    idx = idx + 2
    mothersName = sender_msg[idx:idx + mothersNamelen]
    (statusCode, password)= serverBL.forgotPassword(username, city, birthYear, mothersName)
    return str(command).zfill(2)+str(statusCode).zfill(2)+str(len(password)).zfill(2)+password

while (True):
    rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in rlist:
        # if new client connection add it to list of client sockets. we will use this in the future
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
            print ("open_client_sockets.append(new_socket)")
        else:
            # msg from exiting client
            data = current_socket.recv(1024)
            if data == "":
                open_client_sockets.remove(current_socket)
                print ("Connection with client closed.")
            else:
                (time1, username, command, sender_msg) = parse_header(data)
                ret = 0
                if command == 1:
                    ret = register(time1, username, command, sender_msg)
                elif command == 2:
                    ret = login(time1, username, command, sender_msg)
                elif command == 3:
                    ret = forgotPassword(time1, username, command, sender_msg)
                else:
                    #command unknown
                    ret = str(command).zfill(2) +"99"
                print("sending: " + ret)
                data = str.encode(ret)
                current_socket.send(data)