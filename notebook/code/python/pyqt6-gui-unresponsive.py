import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton,QLabel,QApplication

import time
import psutil

def get_data():
    return psutil.cpu_percent()

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Start Read CPU(the infinite loop)", self)
        btn2.move(150, 50)
        btn2.adjustSize()
      
        btn1.clicked.connect(self.button1Clicked)            
        btn2.clicked.connect(self.button2Clicked)
        
        self.label_1 = QLabel("CPU(%): ", self)
        self.label_1.move(150, 100)
        self.label_1.setStyleSheet("background-color: white;border: 1px solid black;")
   
        self.statusBar()
        
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Read CPU with the infinite loop')
        self.show()
        
        
    def button1Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
    
    def button2Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed') 
        # infinite loop
        while True:
            self.value=get_data()
            self.label_1.setText(f"CPU(%): {self.value}")   
            time.sleep(2)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
