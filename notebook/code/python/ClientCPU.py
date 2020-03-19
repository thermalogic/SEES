from socket import *
from codecs import decode

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
data = decode(server.recv(BUFSIZE), "ascii")
print(data)
server.close()
