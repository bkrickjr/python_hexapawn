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

        self.gen_new_board()

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
        for pawn in self.player_pawns:                                  # for each pawn in player pawn
            if (pawn.get_space() == index):                             # - if the pawn's space is the selected space
                if (self.selected):                                     # -- if there is something selected
                    if (pawn.get_space() == self.selected.get_space()): # --- if the space of the pawn and the selected pawn space are the same
                        print('Already Selected. Deselecting Pawn.')
                        self.clear_selection()                          # ---- deselect the pawn
                        return
                    else:                                               # --- if the space of the pawn and the selected pawn space are different
                        print('Already Selected. Selecting New Pawn.')
                        self.clear_selection()                          # ---- deselect current pawn
                        self.select_pawn(pawn, index)                   # ---- select the pawn
                    # if end
                else:                                                   # -- if there is nothing selected
                    print('Nothing Selected. Selecting Pawn.')                    
                    self.select_pawn(pawn, index)                       # --- select the pawn
                # if end
            # if end
        # for end
    # onclick_board_btn end

    def select_pawn(self, pawn: pawn, index: int):
        '''
        #* Highlight the pawn that was clicked.
        '''
        self.selected = pawn
        self.style_selected(self.btn_list[index])
        moves = pawn.get_moves()
        self.show_moves(moves)
    # select_pawn end

    def clear_selection(self):
        '''
        #* Highlight the pawn that was clicked.
        '''
        self.selected = None
        for btn in self.btn_list: self.style_deselected(btn)
    # clear_selection end

    def show_moves(self, moves: dict):
        '''
        #* Highlight the places the pawn can move or attack.
        '''
        space = self.selected.get_space()
        if (moves['forward']):
            index = space - 3
            self.style_movable(self.btn_list[index])
        # if end

        if (moves['left']):
            index = space - 4
            self.style_attackable(self.btn_list[index])
        # if end

        if (moves['right']):
            index = space - 2
            self.style_attackable(self.btn_list[index])
        # if end
    # show_moves end

    def gen_new_board(self):
        self.gameboard = gameboard.GameBoard()                  # create the board
        self.player_pawns = []                                  # instantiate empty list for player pawns
        self.computer_pawns = []                                # instantiate empty list for copmputer pawns
        for i in range(0, 9):                                   # loop 0-8 for each tile
            if (i < 3):                                         # - if the loop is in the top row
                created_pawn = pawn.Pawn(-1, i, self.gameboard) # -- make computer pawns
                self.computer_pawns.append(created_pawn)        # -- add them to the list
            if (i > 5):                                         # - if the loop is in the bottom row
                created_pawn = pawn.Pawn(1, i, self.gameboard)  # -- make player pawns
                self.player_pawns.append(created_pawn)          # -- add them to the list
        # for end
    # gen_new_board end

    def style_selected(self, btn):
        btn.setStyleSheet("border-color: blue;" "background-color: rgb(170, 170, 15);")
    # style_selected end

    def style_deselected(self, btn):
        btn.setStyleSheet("border-color: black; background-color: rgb(120, 120, 120);")
    # style_deselected end

    def style_movable(self, btn):
        btn.setStyleSheet("border-color: black; background-color: rgb(0, 250, 45);")
    # style_movable end

    def style_attackable(self, btn):
        btn.setStyleSheet("border-color: black; background-color: rgb(250, 0, 0);")
    # style_attackable end

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