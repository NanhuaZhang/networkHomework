import socket
Server_ADDRESS = ('192.168.1.109',1234)
PROXY_ADDRESS = ('127.0.0.1',8000)
cTp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
pTs = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cTp.bind(PROXY_ADDRESS)
print '...waiting for message..'

while True:
    cdata, caddr = cTp.recvfrom(1024)
    print "receive data: %s from %s"%(cdata, caddr)
    # if addr[0] == PROXY_ADDRESS[0]:
    pTs.sendto(cdata,Server_ADDRESS)
    pdata, paddr = pTs.recvfrom(1024)
    print "receive data: %s from %s" % (pdata, paddr)
    cTp.sendto("Server has received messages from address %s." %str(caddr), caddr)
pTs.close()
cTp.close()