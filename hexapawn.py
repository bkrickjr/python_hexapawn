import sys
from PyQt5.QtWidgets import QStyleFactory, QApplication, QMainWindow, QFileDialog, QLineEdit, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        loadUi('gameboard.ui', self)
        self.setStyle(QStyleFactory.create('Fusion'))
    # __init__ end
# class end

def play():
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
# play end
play()