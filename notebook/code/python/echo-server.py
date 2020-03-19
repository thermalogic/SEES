import socket
import psutil
from codecs import encode

def get_data():
    return psutil.cpu_percent()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for connection ...")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = encode(str(round(get_data(),4)),"ascii")
            if not data:
                break
            conn.send(data)
