import socket
import threading
import time
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


HOST = '127.0.0.1' 
PORT = 56789

client_socket = socket.socket()
client_socket.connect((HOST, PORT))
threading.Thread(target=receive, daemon=True).start()
print("connected ok")
import sys
while(1):
    if len(sys.argv) > 1:
        send_commands(sys.argv[1])
        time.sleep(30)
        break
    else:
        print("Usage: python client.py <command_file.txt>")
        time.sleep(30)


client_socket.close()