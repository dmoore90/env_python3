#! /usr/bin/env python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("alarm clock")
   w.setGeometry(2000,1000,300,300)
   b.move(50,20)
   w.setWindowTitle("set time")
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()