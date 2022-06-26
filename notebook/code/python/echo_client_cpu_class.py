from socket import *
from codecs import decode

class  clientcpu:

    def __init__(self, host="localhost", port=5000):
        
        self.host =host
        self.port =port
        self.client_socket = socket(AF_INET, SOCK_STREAM)  # get instance

    def connect(self):
        self.client_socket.connect((self.host, self.port))  # connect to the server

    def receive_data(self, message="cpu"):
        self.client_socket.send(message.encode())  # send message
        self.data = float(decode(self.client_socket.recv(1024), "ascii"))
        return self.data

    def disconnect(self):
        self.client_socket.close()  # close the connection


