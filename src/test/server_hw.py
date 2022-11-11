import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address1 = ('182.160.7.230', 5001)

server_address = ('localhost', 5001)

server.bind(server_address)

server.listen(5)

while True:
    conn, addr = server.accept()

    x = conn.recv(512)
    print(x, addr)