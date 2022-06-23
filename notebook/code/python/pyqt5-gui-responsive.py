import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton,QLabel, QApplication

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

        btn2 = QPushButton("Read CPU with the infinite loop", self)
        btn2.move(150, 50)
        btn2.adjustSize()
      
        btn1.clicked.connect(self.button1Clicked)            
        btn2.clicked.connect(self.button2Clicked)
        
        self.label_1 = QLabel("cpu(%): ", self)
        self.label_1.move(150, 100)
        self.label_1.setStyleSheet("border: 1px solid black;")
               
        self.statusBar()
        
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Unblcoking GUI: Threading IO')
        self.show()
        
        
    def button1Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def io_worker(self):
        """IO thread's worker function"""
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed') 
        while True:
            self.value=get_data()
            self.label_1.setText("cpu(%): "+str(self.value))   
            time.sleep(2)
     
    def button2Clicked(self):
        # Threading IO
        self.t = threading.Thread(target=self.io_worker)
        self.t.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
