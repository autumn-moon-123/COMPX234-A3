import socket
import threading
import time
import sys
import os

def send_commands(filename,stats):

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if command := line.strip():
                cmd_type = command.split(maxsplit=1)[0].upper()
                if cmd_type in ['GET', 'PUT', 'READ']:
                    stats[cmd_type] += 1
                client_socket.sendall(command.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8').strip()
                print(response)
                time.sleep(0.1)


    
if __name__ == "__main__":
    HOST = '127.0.0.1' 
    PORT = 56789
stats = {'GET': 0, 'PUT': 0, 'READ': 0}
client_socket = socket.socket()
client_socket.connect((HOST, PORT))

for i in range(1, 11):
    filename = f"client_{i}.txt"
    if os.path.exists(filename):
        send_commands(filename,stats)
        time.sleep(0.5)


client_socket.close()
print(f"GET : {stats['GET']}")
print(f"PUT : {stats['PUT']}")
print(f"READ : {stats['READ']}")
print(f"Total : {sum(stats.values())}")