import socket
import threading
import time
import sys
import os
def receive():

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"\n[Server] {data}")
        except ConnectionResetError:
            break
        except Exception as e:
            break


def send_commands(filename):
    try:
        if not os.path.exists(filename):
            print(f"[Error] File not found: {filename}")
            return False

        print(f"[Executing: {filename}]")
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if command := line.strip():
                    client_socket.sendall(command.encode('utf-8'))
                    time.sleep(0.1)
        return True
    except Exception as e:
        print(f"[Error] {str(e)}")
        return False
    
def interactive_filename_input():
    print("Enter command file ")
    while True:
        user_input = input("> ").strip()
        if send_commands(user_input):
            print(f"Done")
HOST = '127.0.0.1' 
PORT = 56789

client_socket = socket.socket()
client_socket.connect((HOST, PORT))
threading.Thread(target=receive, daemon=True).start()
print("connected ok")

while(1):
    if len(sys.argv) > 1:
        send_commands(sys.argv[1])
        time.sleep(30)
        break
    else:
        print("Usage: python client.py <command_file.txt>")
        time.sleep(30)


client_socket.close()