import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address1 = ('182.160.7.230', 5001)
server_address = ('localhost', 5001)

client.connect(server_address1)

msg = b'hello bro...'

client.send(msg)

resp = client.recv(1024)
print(resp)
