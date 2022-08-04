import socket

countries_mapping = {
    'pk': 'Pakistan',
    'uk': 'United Kingdom',
    'in': 'India',
    'us': 'United States',
}

# create a TCP, IPV4 socket
server_socket = socket.socket()
# bind host and port
server_socket.bind(('localhost', 8866))
# limit no of active clients
server_socket.listen(10)
print('Waiting for connection')
# accepting client connections
while True:
    client, client_address = server_socket.accept()
    print(f'Connected with {client_address}')
    # accept client's request with data
    data = client.recv(1024).decode('utf-8')
    # send country name to client
    print(f'Received : {data} from client')
    client.send(bytes(f'Country name is: {countries_mapping.get(data)}', 'utf-8'))
    # client.close()



