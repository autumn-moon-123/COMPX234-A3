import socket
import threading

def receive():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"\n{data}")

    open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    print(f"[Sending] {command}")
                    client_socket.send(command.encode('utf-8'))