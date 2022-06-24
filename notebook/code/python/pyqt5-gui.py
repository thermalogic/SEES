import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton,  QLabel,QApplication

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.label_1 = QLabel("", self)
        self.label_1.move(150, 100)
        self.label_1.setStyleSheet("background-color: white; border: 1px solid black;")
 
        self.statusBar()
        
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('The Demo GUI')
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
