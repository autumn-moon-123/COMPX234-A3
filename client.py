import socket
import threading

data = client_socket.recv(1024).decode('utf-8')
print(f"\n{data}")