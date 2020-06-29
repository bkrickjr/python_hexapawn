import gameboard
import log
import sys
from ai import AI
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
        self.debug_log = log.Log('Hexapawn Debug -')
        self.btn_debug.clicked.connect(lambda: print(self.debug_log))
        self.update_log('Player Moves First')

        self.win_count_player = 0
        self.win_count_computer = 0
        self.win_count_draw = 0

        self.game_state = 'player turn'

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
        self.btn_new_game.clicked.connect(self.new_game)
        self.btn_play_again.clicked.connect(self.play_again)

        self.game_board = gameboard.GameBoard(self.btn_list)
        self.computer = AI(self.game_board, self.log, self.debug_log)
        self.play_again()
    # __init__ end

    def new_game(self):
        self.computer.learn('win')
        for btn in self.btn_list:
            btn.setEnabled(True)
        # for end
        self.selected = None
        self.turn = 1
        self.game_board.reset_board()
        self.btn_new_game.setEnabled(True)
        self.btn_play_again.setEnabled(False)
    # new_game end

    def play_again(self):
        for btn in self.btn_list:
            btn.setEnabled(True)
        # for end
        self.selected = None
        self.turn = 1
        self.game_board.reset_board()
        self.btn_new_game.setEnabled(True)
        self.btn_play_again.setEnabled(False)
    # play_again end

    def check_win(self):
        self.debug_log.add('check_win begin.')

        toprow = self.game_board.get_top_row()  # Player Pawn Reached Top
        for tile in toprow:
            self.debug_log.add('Top Row position %s, controlled %s'%(tile.get_pos(), tile.get_controlled()))
            if (tile.get_controlled() == 1):
                self.debug_log.add('Player Pawn Found')
                self.game_over('Player Win!')
                return True
            # if end
        # for end

        botrow = self.game_board.get_bot_row() # Computer Pawn Reached Bottom
        for tile in botrow:
            self.debug_log.add('Bot Row position %s, controlled %s'%(tile.get_pos(), tile.get_controlled()))
            if (tile.get_controlled() == -1):
                self.debug_log.add('Computer Pawn Found')
                self.game_over('Computer Win!')
                return True
            # if end
        # for end

        gb_state = self.game_board.get_game_state()

        if (not 1 in gb_state):               # Computer Captured All Player Pawns
            self.game_over('Computer Win!')
            return True
        # if end

        if (not -1 in gb_state):              # Player Captured All Computer Pawns
            self.game_over('Player Win!')
            return True
        # if end

        draw00 = [-1,  0,  0,  1,  0, -1,  0,  0,  1]
        draw01 = [ 0,  0, -1, -1,  0,  1,  1,  0,  0]
        draw02 = [ 0, -1,  0,  0,  1,  0,  0,  0,  0]
        draw03 = [-1,  0,  0,  1, -1,  0,  0,  1,  0]
        draw04 = [ 0,  0, -1,  0, -1,  1,  0,  1,  0]
        draw05 = [ 0, -1,  0,  0,  1, -1,  0,  0,  1]
        draw06 = [ 0, -1,  0, -1,  1,  0,  1,  0,  0]
        draw07 = [ -1,  0, -1,  1, -1, 1,  0,  1,  0]
        draws = [draw00, draw01, draw02, draw03, draw04, draw05, draw06, draw07]
        if (gb_state in draws):               # Draw
            self.game_over('Draw!')
            return True
        # if end

        self.debug_log.add('No Winner Turn %s'%(self.turn))
        return False
    # check_win end

    def game_over(self, msg):
        self.btn_new_game.setEnabled(False)
        self.btn_play_again.setEnabled(True)
        for btn in self.btn_list:
            btn.setEnabled(False)
        # for end
        self.update_log(msg)
        if ('Computer' in msg):
            self.win_count_computer += 1
            computer_result = 'win'
        elif ('Player' in msg):
            self.win_count_player += 1
            computer_result = 'loss'
        else:
            self.win_count_draw += 1
            computer_result = 'draw'
        # if end
        self.update_labels(self.win_count_player, self.win_count_computer)
        self.computer.learn(computer_result)
    # game_over end

    def onclick_board_btn(self, index):
        tile_clicked = self.game_board.tiles[index]          # get the tile
        if (not self.selected):                              # if nothing was previously selected
            if (tile_clicked.get_controlled() == 1):         # - if the tile_clicked is owned by the player (1)
                self.debug_log.add('Nothing selected, selecting %s'%(tile_clicked))
                self.select_tile(tile_clicked)               # -- select the tile
                return                                       # -- return
            # if end
        # if end

        if (self.selected):                                  # if there is something selected
            self.debug_log.add('Something already selected')
            controlled = tile_clicked.get_controlled()
            if (controlled == 1):                            # - if the tile_clicked is owned by the player (1), switching selection
                self.debug_log.add('Selecting another player pawn')
                self.game_board.unselect_all()               # -- clear all the formatting
                self.select_tile(tile_clicked)               # -- select the tile
            # if end

            if (controlled == 0):                            # - if the tile_clicked is an open space (0), check if it's movable
                self.debug_log.add('Empty Tile Clicked %s'%(tile_clicked))
                if (tile_clicked.is_movable(self.selected)): # -- if the tile_clicked is movable
                    self.debug_log.add('Tile is movable')
                    self.player_move(tile_clicked)
                else:                                        # -- if the tile_clicked is not movable
                    self.debug_log.add('Tile is not movable')
                    self.game_board.unselect_all()           # --- clear all the formatting
                    self.selected = None                     # --- deselect the current tile
                # if end
            # if end

            if (controlled == -1):
                self.debug_log.add('Enemy Tile Clicked %s'%(tile_clicked))
                if (tile_clicked.is_attackable(self.selected)): # -- if the tile_clicked is movable
                    self.debug_log.add('Tile is attackable')
                    self.player_move(tile_clicked)
                else:                                        # -- if the tile_clicked is not movable
                    self.debug_log.add('Tile is not attackable')
                    self.game_board.unselect_all()           # --- clear all the formatting
                    self.selected = None                     # --- deselect the current tile
                # if end
            # if end
        # if end
    # onclick_board_btn

    def player_move(self, tile_clicked):
        self.selected.change_control(0)          # --- remove player from currently selected
        tile_clicked.change_control(1)           # --- move player to tile_clicked
        self.game_board.unselect_all()           # --- clear all the formatting
        self.update_log('Turn %s: Player moved from position %s to %s'%(self.turn, self.selected.get_pos(), tile_clicked.get_pos()))
        self.selected = None                     # --- deselect the current tile
        won = self.check_win()
        if (not won):
            self.next_turn()
        # if end
    # player_move end

    def next_turn(self):
        if (self.turn == 1):
            self.computer.turn2()
            self.turn += 2
            won = self.check_win()
            return
        # if end
        if (self.turn == 3):
            self.computer.turn4()
            self.turn += 2
            won = self.check_win()
            return
        # if end
        if (self.turn == 5):
            self.computer.turn6()
            self.turn += 2
            won = self.check_win()
            return
        # if end        
    # next_turn end

    def select_tile(self, tile):
        self.selected = tile
        self.game_board.show_moves(tile.get_pos())
        tile.style_button(tile._style_selected)
    # select_tile end

    def update_labels(self, player_wins, computer_wins):
        self.lbl_score_player.setText('Player Wins: %s'%(player_wins))
        self.lbl_score_computer.setText('Computer Wins: %s'%(computer_wins))
    # update_labels end

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