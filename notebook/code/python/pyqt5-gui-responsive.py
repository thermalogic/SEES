import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

import time
import psutil
import threading

def get_data():
    return psutil.cpu_percent()

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
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

    def io_worker(self):
        """thread's worker function"""
        while True:
            self.value=get_data()
            self.statusBar().showMessage(str(self.value))  
            time.sleep(2)
     
    def button2Clicked(self):
        # Threading IO
        self.t = threading.Thread(target=self.io_worker)
        self.t.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
