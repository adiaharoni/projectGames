from time import sleep
import clientComm

_fe_login_res = None
_fe_register_res = None
_fe_forgot_password_res = None
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
        print("BL status_code=" + str(status_code) + " text:" + status_txt+ " password: "+ str(password))
    else:
        print("BL status_code=" + str(status_code) + " text:" + status_txt )
    global _fe_forgot_password_res
    _fe_forgot_password_res(status_code, status_txt, password)