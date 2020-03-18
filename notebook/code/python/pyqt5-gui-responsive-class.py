import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

import time
import psutil
import threading

def get_data():
    return psutil.cpu_percent()

class MonitorThread(threading.Thread):
    """ A thread clacc for monitoring a CPU. """

    def __init__(self,ON,valueUI):
        threading.Thread.__init__(self)
        self.value =None
        self.ON=ON
        self.valueUI=valueUI

    def run(self):
        while True:
            if self.ON==True:
                self.value = get_data()
            else:
                self.value="Paused"
            self.valueUI.showMessage(str(self.value))
            time.sleep(2)

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cpu_monitor=None
        
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
      
    def button2Clicked(self):
        if self.cpu_monitor==None:
            self.cpu_monitor = MonitorThread(True,self.statusBar())
            self.cpu_monitor.start()
        else:
            self.cpu_monitor.ON = not self.cpu_monitor.ON 
              
        text = self.btn2.text()
        self.btn2.setText("To Pause" 
                          if text == "Start CPU" else "Start CPU")   
      
             
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
