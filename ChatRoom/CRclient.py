#coding:utf-8
import socket
import threading
BUFF_SIZE = 1024
Server_ADDRESS = ("127.0.0.1", 8001)


def conn():
    cs = socket.socket()
    cs.connect(Server_ADDRESS)
    return cs


def register(s):
    while True:
        RegisterData = "rg"+raw_input("Do you have an account?If not,please register an account.yes or no?\n")
        s.send(RegisterData)
        print s.recv(BUFF_SIZE)
        s.send("RegisterName "+raw_input())
        print s.recv(BUFF_SIZE)
        s.send("RegisterPassword "+raw_input())
        print s.recv(BUFF_SIZE)


def login(s):
    s.send("Input you account:")
    name = s.recv(BUFF_SIZE)
    s.send("Input you password:")
    password = s.recv(BUFF_SIZE)


def main():
    c_socket = conn()
    t1 = threading.Thread(target=register,args=(c_socket,))
    t1.start()
    # register(c_socket)

if __name__ == '__main__':
    main()
