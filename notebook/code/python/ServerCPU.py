"""
Server for providing the cpu_percent.
"""
from socket import *
import psutil
from codecs import encode


def get_data():
    return psutil.cpu_percent()

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print("Waiting for connection ...")
    (client, address) = server.accept()
    print("... connected from: ", address)
    data = encode(str(round(get_data(),4)),"ascii")
    print(data)
    client.send(data)
    client.close()

