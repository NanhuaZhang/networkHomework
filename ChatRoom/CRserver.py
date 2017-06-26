#coding:utf-8
import socket
import select
BUFF_SIZE = 1024
Server_ADDRESS = ("127.0.0.1", 8001)
accounts = []
inputs = []
# account = ["root", "123"]


def conn():
    ss = socket.socket()
    ss.bind(Server_ADDRESS)
    ss.listen(5)
    return ss


def login(s):
    s.send("Input you account:")
    name = s.recv(BUFF_SIZE)
    s.send("Input you password:")
    password = s.recv(BUFF_SIZE)


def register(s):
    account = []
    c_socket, addr = s.accept()
    while True:
        data = c_socket.recv(BUFF_SIZE)
        print data
        if data.split(' ')[0] == "RegisterName":
            account.append(data.split(' ')[1])
            c_socket.send("Input you password:")
        if data.split(' ')[0] == "RegisterPassword":
            account.append(data.split(' ')[1])
            c_socket.send("RegisterComplete,please login.")
        if data == "rgno":
            c_socket.send("Input you account:")
        elif data == "rgyes":
            c_socket.send("Please login.")
            break
        if len(account) == 2:
            accounts.append(account)
            account = []
    inputs.append(c_socket)


def running():
    print "Running..."
    c_socket = conn()
    inputs.append(c_socket)
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            if r is c_socket:
                register(r)
            else:
                pass

if __name__ == '__main__':
    running()