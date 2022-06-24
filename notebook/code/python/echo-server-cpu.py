from socket import *

import psutil
from codecs import encode

def get_data():
    return psutil.cpu_percent()

def server_program():
    bufsize = 1024
    host = "localhost"
    #host = gethostname()
    port = 5000  # initiate port no above 1024
    
    server_socket = socket(AF_INET, SOCK_STREAM)# get instance
    # server_socket = socket()
    # look closely. The bind() function takes tuple as argument
    address = (host, port)
    server_socket.bind(address)  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    print("Waiting for connection ...")
    
    # accept new connection
    while True:
        conn, address = server_socket.accept()  
        print("Connection from: " + str(address))
        # the nested loop
        while True:
            try:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(bufsize).decode()
                if not data:
                    # if data is not received break
                    break
                print("from connected user: " + str(data))
                data = encode(str(round(get_data(),4)),"ascii")
                conn.send(data)  # send data to the client
            except:
                break
            
        conn.close()  # close the connection
    
if __name__ == '__main__':
    server_program()
