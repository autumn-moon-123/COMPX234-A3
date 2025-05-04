import socket
import threading

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
        if ' ' not in data:
            response = "ERROR: Wrong order"
        else:
            cmd, content = data.split(maxsplit=1)
            if cmd == "READ":
                response = f"SERVER:{kv.read(content)}"
            elif cmd == "GET":
                response = f"SERVER:{kv.get(content)}"
            elif cmd == "PUT":
                cmd1,content1=content.split(maxsplit=1)
                response = f"LAB:{kv.put(cmd1, content1)}"
            else:
                response = "ERROR: Unknown command"
        mysocket.send(response.encode())