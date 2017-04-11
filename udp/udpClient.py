import socket
PROXY_ADDRESS=("127.0.0.1",8000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    message=raw_input("input some messages.\n")
    s.sendto(message,PROXY_ADDRESS)
    date=s.recv(1024)
    print(date)
s.close()