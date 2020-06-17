import gameboard
import log
import pawn
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

        self.selected = None

        self.generate_board()

        self.btn0.clicked.connect(lambda: self.onclick_board_btn(0))
        self.btn1.clicked.connect(lambda: self.onclick_board_btn(1))
        self.btn2.clicked.connect(lambda: self.onclick_board_btn(2))
        self.btn3.clicked.connect(lambda: self.onclick_board_btn(3))
        self.btn4.clicked.connect(lambda: self.onclick_board_btn(4))
        self.btn5.clicked.connect(lambda: self.onclick_board_btn(5))
        self.btn6.clicked.connect(lambda: self.onclick_board_btn(6))
        self.btn7.clicked.connect(lambda: self.onclick_board_btn(7))
        self.btn8.clicked.connect(lambda: self.onclick_board_btn(8))
        self.btn_list = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8]

    # __init__ end

    def onclick_board_btn(self, index: int):
        '''
        #* Handle the clicks of the game tiles.
        '''
        print('pawn clicked index %s'%(index))
        # if nothing is selected or what is selected is not what was clicked
        for pawn in self.player_pawns:
            if (pawn.get_space() == index):
                resp = pawn.get_moves()
                self.selected = pawn
                self.style_selected(self.btn_list[index])
            # if end
        # for end
    # onclick_board_btn end

    def generate_board(self):
        self.gameboard = gameboard.GameBoard()                          # create the board
        self.player_pawns = []
        self.computer_pawns = []
        for i in range(0, 9):                                           # loop 0-8 for each tile
            if (i < 3): 
                created_pawn = pawn.Pawn('Computer', i, self.gameboard) # - if the loop is in the top row, make computer pawns
                self.computer_pawns.append(created_pawn)
            if (i > 5): 
                created_pawn = pawn.Pawn('Player', i, self.gameboard)   # - if the loop is in the bot row, make player pawns
                self.player_pawns.append(created_pawn)
        # for end
    # generate_board end

    def style_selected(self, btn):
        print('attempting to style as selected')
        btn.setStyleSheet("border-color: blue;" "background-color: rgb(170, 170, 15);")
    # style_selected end

    def style_deselected(self, btn):
        print('attempting to style as deselected')
        btn.setStyleSheet("border-color: black; background-color: rgb(120, 120, 120);")
    # style_deselected end

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