
import psutil
from socket import *
import threading
from codecs import encode

class ClientThread(threading.Thread):

    def __init__(self,conn,address, bufsize):
        threading.Thread.__init__(self)
        self.bufsize=bufsize
        self.conn = conn
        self.address=address
        print ("New connection added: ", address)
    
    def run(self):
        # the nested loop
        while True:
            try:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = self.conn.recv(self.bufsize).decode()
                if not data:
                    # if data is not received break
                    break
                print("from connected user: " + str(data))
                data = encode(str(round(get_data(),4)),"ascii")
                self.conn.send(data)  # send data to the client
            except:
                break
   
        self.conn.close()# close the connection
        print ("Client at ", self.address , " disconnected...")

        
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
    
    while True:
        conn, address =  server_socket.accept()
        newthread = ClientThread(conn, address, bufsize)
        newthread.start()
            
if __name__ == '__main__':
    server_program()           
