import log
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

        self.log = log.Log('Welcome to Hexapawn!')
        self.update_log('Player Moves First')
    # __init__ end

    def update_log(self, addition: str):
        '''
        #* Update the log that is displayed to the Player.\n
        # @param addition: String - The addition to the log.
        '''
        self.log.add(addition)
        self.tE_log.setText(self.log.__str__())
    # update_log end
# class end

def play():
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
# play end
play()