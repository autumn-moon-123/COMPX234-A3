import socket
import threading
import time
import sys
import os

def send_commands(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if command := line.strip():
                client_socket.sendall(command.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8').strip()
                print(response)
                time.sleep(0.1)


    
if __name__ == "__main__":
    HOST = '127.0.0.1' 
    PORT = 56789

client_socket = socket.socket()
client_socket.connect((HOST, PORT))

for i in range(1, 11):
    filename = f"client_{i}.txt"
    if os.path.exists(filename):
        send_commands(filename)
        time.sleep(0.5)


client_socket.close()