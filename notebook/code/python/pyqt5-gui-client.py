import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtCore

import time
import psutil
import threading

from socket import *
from codecs import decode

class MonitorThread(threading.Thread):
    """ A thread clacc for monitoring a CPU. """

    def __init__(self,ON):
        threading.Thread.__init__(self)
        self.value =None
        self.ON=ON
        
        HOST = "localhost"
        PORT = 5000
        self.BUFSIZE = 1024
        self.ADDRESS = (HOST, PORT)
        self.server = socket(AF_INET, SOCK_STREAM)
          
    def run(self):
        while True:
            if self.ON==True:
                self.server = socket(AF_INET, SOCK_STREAM)
                self.server.connect(self.ADDRESS)
                self.value  = decode(self.server.recv(self.BUFSIZE), "ascii")
                self.server.close()
            else:
                pass
            time.sleep(2)
            
            

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cpu_monitor=None
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.on_timer)
              
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        self.btn2 = QPushButton("Start CPU", self)
        self.btn2.move(150, 50)
      
        btn1.clicked.connect(self.button1Clicked)            
        self.btn2.clicked.connect(self.button2Clicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Threading IO')
        self.show()
        
    def button1Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
      
    def on_timer(self):
        """Executed periodically """
        if self.cpu_monitor.ON:
            self.statusBar().showMessage(str(self.cpu_monitor.value))
        
    def button2Clicked(self):
        self.statusBar().showMessage("")
        if self.cpu_monitor==None:
            self.cpu_monitor = MonitorThread(True)
            self.cpu_monitor.start()
            self.timer.start(2000)  
            self.statusBar().showMessage("Staring")
        else:
            self.cpu_monitor.ON = not self.cpu_monitor.ON 
            
        if self.cpu_monitor.ON: 
            self.btn2.setText("To Pause")
            self.statusBar().showMessage("Staring")
        else: 
            self.btn2.setText("To Start")
            self.statusBar().showMessage("Paused")
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
