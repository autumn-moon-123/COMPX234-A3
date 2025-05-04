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