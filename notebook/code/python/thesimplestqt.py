import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow

class Example(QMainWindow): 
    
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Simple')
        self.show()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv) # 1 Every PyQt5 applicationmust create an application object.
    ex=Example()                 # 2 create GUI in memory and later show on the screen.
    sys.exit(app.exec_())  # 3 The sys.exit() method ensures a clean exit. 
