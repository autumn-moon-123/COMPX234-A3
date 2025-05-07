import socket
import threading
import time
import sys
import os

def send_commands(filename):
  try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if command := line.strip():
                client_socket.sendall(command.encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8').strip()
                print(response)
                time.sleep(0.1)
        return True
  except Exception as e:
        print(f"[Error] {str(e)}")
        return False
    
if __name__ == "__main__":
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