from socket import *

Server_ADDRESS=('192.168.1.109',1234)
s = socket(AF_INET, SOCK_DGRAM)
s.bind(Server_ADDRESS)
print '...waiting for message..'
while True:
    data, address = s.recvfrom(1024)
    print "receive data: %s from %s" % (data, address)
    s.sendto('Hi,proxyServer.I have receive data: %s from address %s' %(data,address), address)
s.close()