import socket
import threading
import time
class Valuestore:
    def __init__(self):
        self.store = {} 
        self.lock = threading.Lock()
    def read(self, k):
        with self.lock:
         return self.store.get(k, "")
    def get(self, k):
        with self.lock:
            return self.store.pop(k, "")
    def put(self, k, v):
        if len(f"{k} {v}") > 970:
            return 2
        with self.lock:
            if k in self.store:
                return 1  
            self.store[k] = v
            return 0 
        
kv = Valuestore()
def myclient(mysocket,address):
    while True:
        data = mysocket.recv(1024).decode('utf-8').strip()
        if not data:
            break
        if '_' in data and data.split('_')[0] in ['READ', 'GET', 'PUT']:
            data = data.replace('_', ' ', 1)

        cmd, content = data.split(maxsplit=1)
        
        if cmd == "READ":
            value = kv.read(content)
            response = f"READ {content}: OK ({content}, {value}) read" if value else f"READ {content}: ERR {content} does not exist"

        elif cmd == "GET":
            value = kv.get(content)
            response = f"GET {content}: OK ({content}, {value}) removed" if value else f"GET {content}: ERR {content} does not exist"

        elif cmd == "PUT":
            k, v = content.split(maxsplit=1)
            status = kv.put(k, v)
            if status == 0:
                response = f"PUT {k} {v}: OK ({k}, {v}) added"
            elif status == 1:
                response = f"PUT {k} {v}: ERR {k} exists"
            else:
                response = f"PUT {k} {v}: ERR value too long"

        mysocket.send(response.encode())
HOST = '127.0.0.1'
PORT = 56789
def printallstore():
    while True:
        with kv.lock:
            storecopy = kv.store.copy()  

        print("\n10s output") 
        for k, v in storecopy.items():
            print(f"{k}: {v}")  
        time.sleep(10)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f" start server {HOST}:{PORT}...")
print_thread = threading.Thread(
    target=printallstore,
    daemon=True
)
print_thread.start()
try:
    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=myclient, args=(client_socket, address)).start()

except KeyboardInterrupt:
        print("\n stop..")
finally:
        server_socket.close()