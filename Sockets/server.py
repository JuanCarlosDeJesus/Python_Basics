# Socket
# End point of communication between two machines
# Socket is an interface between application layer and transport layer
# UDP and TCP are two types of sockets

import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP
# UDP faster than TCP but less reliable
# Connect to a server
s.bind(('127.0.0.1', 55555)) # Bind the socket to an address and port localhost = 127.0.0.1
s.listen() # Listen for incoming connections, 5 is the maximum number of queued connections

while True:
    conn, addr = s.accept() # Accept a connection, returns a new socket object and the address of the client
    print(f'Connection from {addr}')
    conn.send("Hello, World!".encode()) # Send a message to the client, encode() converts the string to bytes
    conn.close() # Close the connection
