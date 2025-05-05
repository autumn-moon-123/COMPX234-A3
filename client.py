import socket
import threading

def receive():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"\n{data}")

def send_commands(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    print(f"[Sending] {command}")
                    client_socket.send(command.encode('utf-8'))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error reading file: {e}")
    finally:
        client_socket.close()
