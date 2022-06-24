
from socket import *
import time
from codecs import decode


def client_program():
    # host = socket.gethostname()
    host = "localhost"  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket(AF_INET, SOCK_STREAM)  # get instance
    # client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "cpu"
    while True:
        try:
            client_socket.send(message.encode())  # send message
            data = decode(client_socket.recv(1024), "ascii")
            print('Received from server: ' + data)  # show in terminal
            time.sleep(1)
            message = "cpu"
        except KeyboardInterrupt:  # Press 'Ctrl + C' to  close the connection
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break
    
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
