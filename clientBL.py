from time import sleep
import clientComm

def get_srv_res_status():
    (status_code, status_txt) = clientComm.get_srv_res_status()
    while (status_code==None):
        (status_code, status_txt) = clientComm.get_srv_res_status()
        sleep(0.05)
    return (status_code, status_txt)

clientComm.init()
clientComm.register("guy", "1234", "hod hasharon", "1972", "neora")
(status_code, status_txt) =get_srv_res_status()
print("status_code=" + str(status_code) + " text:" + status_txt)

clientComm.login("guy", "1234")
(status_code, status_txt) =get_srv_res_status()
print("status_code=" + str(status_code) + " text:" + status_txt)

clientComm.forgot_password("guy", "hod hasharon", "1972", "neora")
(status_code, status_txt, password) = clientComm.get_forgot_password_res()
while (status_code == None):
    (status_code, status_txt, password) = clientComm.get_forgot_password_res()
    sleep(0.05)
print("status_code=" + str(status_code) + " text:" + status_txt + " password:" + password)
