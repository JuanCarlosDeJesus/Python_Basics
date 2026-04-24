import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP
s.connect(('127.0.0.1', 55555)) # Connect to the server, localhost = 127.0.0.1
message = s.recv(1024) # Receive a message from the server, 1024 is the buffer size
s.close() # Close the connection
print(message.decode()) # Decode the message from bytes to string and print it