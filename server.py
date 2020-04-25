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
    # command
    idx=0
    command = int(recvdata[idx:idx + 2])
    print("command:"+recvdata[idx:idx + 2])
    idx = idx + 2
    time1 = recvdata[idx:idx+14]
    print("time1:"+time1)
    idx = idx+14
    namelen = int(recvdata[idx:idx + 2])
    print ("namelen:"+recvdata[idx:idx + 2])
    idx = idx + 2
    username = recvdata[idx:idx + namelen]
    print("username:"+username)
    idx = idx + namelen
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

def login(socket, time1, username, command, sender_msg):
    passwordlen = int(sender_msg[0:2])
    idx = 2
    password = sender_msg[idx:idx + passwordlen]
    statusCode = serverBL.login(username, password)
    if statusCode == 0:
        users[username] = socket
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


def startGame(username, gameId, gameNumber, score , opponentUsername, opponentScore, opponentGameNumber):
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    print("username: "+ username + " gameId: " + gameId+ " gameNumber:" +gameNumber+ " score: "+ str(score) + " opponentUsername: " +opponentUsername+ " opponentScore:" + str(opponentScore)+ " opponentGameNumber: "+opponentGameNumber)

    strScore =str(score)
    sender_message = str(gameId).zfill(2) + str(gameNumber) + str(len(strScore)).zfill(2) + strScore
    sender_message += str(len(str(opponentScore))).zfill(2) + str(opponentScore) + str(opponentGameNumber)
    str_data = "05" + time + str(len(opponentUsername)).zfill(2) + opponentUsername + sender_message
    print("start game:"+ str_data)
    messages_to_send.append((users[username], str.encode(str_data)))


def wantToPlay(time1, username, command, sender_msg):
    gameID = sender_msg[0:2]
    gameNumber = sender_msg[2:]
    print("gameID:"+ gameID + " gameNumber:"+ gameNumber)
    (statusCode, username, score, gameNumber, username1, score1, gameNumber1) = serverBL.wantToPlay(username, gameID, gameNumber)
    ret = str(command).zfill(2)+str(statusCode).zfill(2) + str(gameNumber)
    if statusCode == 9:
        startGame(username1, gameID, gameNumber1, score1, username, score, gameNumber)
        ret = ret + str(len(str(score))).zfill(2)+ str(score) + str(len(username1)).zfill(2) + username1 + str(len(str(score1))).zfill(2) + str(score1) + str(gameNumber1)
    return ret

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
                for username, socket in users.items():
                    if socket == current_socket:
                        del users[username]
                print ("Connection with client closed.")
            else:
                (time1, username, command, sender_msg) = parse_header(data)
                ret = 0
                if command == 1:
                    ret = register(time1, username, command, sender_msg)
                elif command == 2:
                    ret = login(current_socket, time1, username, command, sender_msg)
                elif command == 3:
                    ret = forgotPassword(time1, username, command, sender_msg)
                elif command == 4:
                    ret = wantToPlay(time1, username, command, sender_msg)
                else:
                    #command unknown
                    ret = str(command).zfill(2) + "99"
                print("sending: " + ret)
                data = str.encode(ret)
                current_socket.send(data)
    send_waiting_messages(wlist)