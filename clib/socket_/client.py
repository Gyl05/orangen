import socket


messages = ['This is the message ', 'It will be sent ', 'in parts ', ]

server_address = ('localhost', 8090)
# 创建三个 client socket 
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET,  socket.SOCK_STREAM), ]

print (f'connecting to {server_address[0]} port {server_address[1]}')
for s in socks:
    s.connect(server_address)

for index, message in enumerate(messages):
    # Send messages on both sockets
    for s in socks:
        print ('%s: sending "%s"' % (s.getsockname(), message + str(index)))
        s.send(bytes(message + str(index)).decode('utf-8'))
    # Read responses on both sockets

for s in socks:
    data = s.recv(1024)
    print ('%s: received "%s"' % (s.getsockname(), data))
    if data != "":
        print ('closingsocket', s.getsockname())
        s.close()