import socket

# create a TCP, IPV4 socket
client_socket = socket.socket()
# connect to server
client_socket.connect(('localhost', 8866))
# first message after connecting
client_socket.send(bytes('us', 'utf-8'))
# receiving country name from server
print(client_socket.recv(1024).decode('utf-8'))
