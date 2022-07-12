
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'alarm clock'
        self.left = 1000
        self.top = 1000
        self.width = 640
        self.height = 480
        self.initUI()

        pybutton = QPushButton('click me', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50,50)

    def clickMethod(self):
        print('Clicked')
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())