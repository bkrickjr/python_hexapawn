import random
from gameboard import GameBoard
from tile import Tile

class AI():
    def __init__(self, gameboard, log, debug):
        self.log = log
        self.debug_log = debug
        self.gb = gameboard
        self.movesetT2 = {'board01': [(1, 3), (1, 4), (2, 5)], 'board02': [(0, 3), (0, 4), (2, 4), (2, 5)], 'board03': [(0, 3), (1, 4), (1, 5)]}
        self.optionT2 = None
        self.moveset_T4 = None
        self.optionT4 = None
        self.moveset_T6 = None
        self.optionT6 = None
    # __init__ end

    def get_options(self, board, moveset):
        length = moveset[board].__len__()
        rand_num = random.randrange(length)
        return moveset[board][rand_num]
    # get_options end

    def take_turn(self, start, move):
        tiles = self.gb.tiles
        tiles[start].change_control(0)
        tiles[move].change_control(-1)
    # take_turn

    def turn2(self):
        state = self.gb.get_game_state()
        board01 = [-1, -1, -1, 1, 0, 0, 0, 1, 1]
        board02 = [-1, -1, -1, 0, 1, 0, 1, 0, 1]
        board03 = [-1, -1, -1, 0, 0, 1, 1, 1, 0]

        if (state == board01):
            board = 'board01'
        elif (state == board02):
            board = 'board02'
        elif (state == board03):
            board = 'board03'
        else:
            msg = 'uh oh! bad board state %s'%(state)
            self.log.add(msg)
            self.debug_log.add(msg)
            return
        # if end
        self.debug_log.add(board)
        self.optionT2 = self.get_options(board, self.movesetT2)
        self.debug_log.add(self.optionT2)
        start_pos = self.optionT2[0]
        move_pos = self.optionT2[1]
        self.take_turn(start_pos, move_pos)
        
        self.log.add('Turn 2: Computer moves from position %s to %s'%(start_pos, move_pos))
    # turn2 end
# class end