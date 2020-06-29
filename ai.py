import random
from gameboard import GameBoard
from tile import Tile

class AI():
    def __init__(self, gameboard, log, debug):
        self.log = log
        self.debug_log = debug
        self.gb = gameboard
        self.movesetT2 = {'board01': [(1, 3), (1, 4), (2, 5)],
            'board02': [(0, 3), (0, 4), (2, 4), (2, 5)],
            'board03': [(0, 3), (1, 4), (1, 5)]}
        self.boardT2 = None
        self.optionT2 = None
        self.movesetT4 = {'board01': [(0, 4), (2, 4), (2, 5), (3, 6)],
            'board02': [(0, 3), (0, 4), (2, 4), (5, 8)],
            'board03': [(1, 3), (2, 5), (4, 7)],
            'board04': [(0, 3), (1, 5), (4, 7)],
            'board05': [(0, 4), (2, 4), (2, 5)],
            'board06': [(0, 3), (0, 4), (2, 4)],
            'board07': [(1, 3), (1, 4), (1, 5)],
            'board08': [(1, 3), (1, 4), (1, 5)],
            'board09': [(1, 3), (1, 4), (1, 5)],
            'board10': [(1, 3), (1, 4), (1, 5)],
            'board11': [(1, 5), (4, 6), (4, 7)],
            'board12': [(1, 3), (4, 7), (4, 8)],
            'board13': [(1, 5), (2, 4)],
            'board14': [(3, 6), (3, 7)],
            'board15': [(5, 7), (5, 8)],
            'board16': [(0, 4), (1, 3)],
            'board17': [(2, 4), (2, 5)],
            'board18': [(0, 3), (0, 4)],
            'board19': [(2, 4), (2, 5)],
            'board20': [(0, 3), (0, 4)], 
            'board21': [(2, 5)],
            'board22': [(0, 3)]}
        self.boardT4 = None
        self.optionT4 = None
        self.movesetT6 = {'board01': [(3, 6), (4, 7)],
            'board02': [(4, 7), (5, 8)],
            'board03': [(0, 4)],
            'board04': [(2, 4)],
            'board05': [(1, 5), (3, 7)],
            'board06': [(1, 3), (5, 8)],
            'board07': [(3, 6), (4, 7)],
            'board08': [(4, 7), (5, 8)],
            'board09': [(2, 4), (2, 5), (4, 7)],
            'board10': [(0, 3), (0, 4), (5, 8)],
            'board11': [(1, 3), (4, 7)],
            'board12': [(1, 5), (4, 7)],
            'board13': [(0, 4), (3, 7)],
            'board14': [(2, 4), (5, 8)] }
        self.boardT6 = None
        self.optionT6 = None
    # __init__ end

    def get_options(self, board, moveset):
        '''
        #* Get the options of moves available to the AI at this state in the game.\n
        # @param board: String - The board states for each move are set to 'board01', 'board02', ect.\n
        # @param moveset: Dictionary - The dictionary to look up the board state in.
        '''
        length = moveset[board].__len__()
        rand_num = random.randrange(length)
        return moveset[board][rand_num]
    # get_options end

    def learn(self, result):
        '''
        #* Learn from the game played.\n
        #* Win - Add the moves 3x.\n
        #* Draw - Add the moves 1x.\n
        #* Loss - Remove the moves 1x.
        # @param result: String - The Computer's win/loss/draw.
        '''
        self.debug_log.add('Pre-Learn:------------')
        if (self.boardT2): self.debug_log.add(self.movesetT2[self.boardT2])
        if (self.boardT4): self.debug_log.add(self.movesetT4[self.boardT4])
        if (self.boardT6): self.debug_log.add(self.movesetT6[self.boardT6])
        
        if (result == 'win'):                                                      # if the computer won
            self.movesetT2[self.boardT2].append(self.optionT2)                     # - add the option to the moveset again for Turn2
            self.movesetT2[self.boardT2].append(self.optionT2)                     # - add the option to the moveset again for Turn2
            self.movesetT2[self.boardT2].append(self.optionT2)                     # - add the option to the moveset again for Turn2
            self.movesetT4[self.boardT4].append(self.optionT4)                     # - add the option to the moveset again for Turn4
            self.movesetT4[self.boardT4].append(self.optionT4)                     # - add the option to the moveset again for Turn4
            self.movesetT4[self.boardT4].append(self.optionT4)                     # - add the option to the moveset again for Turn4
            if (self.optionT6): self.movesetT6[self.boardT6].append(self.optionT6) # - add the option to the moveset again for Turn6
            if (self.optionT6): self.movesetT6[self.boardT6].append(self.optionT6) # - add the option to the moveset again for Turn6
            if (self.optionT6): self.movesetT6[self.boardT6].append(self.optionT6) # - add the option to the moveset again for Turn6
        elif (result == 'draw'):
            self.movesetT2[self.boardT2].append(self.optionT2)                     # - add the option to the moveset again for Turn2
            self.movesetT4[self.boardT4].append(self.optionT4)                     # - add the option to the moveset again for Turn4
            if (self.optionT6): self.movesetT6[self.boardT6].append(self.optionT6) # - add the option to the moveset again for Turn6
        elif (result == 'loss'):                                                   # if the computer lost
            option_list_len_T2 = self.movesetT2[self.boardT2].__len__()            # - check the length of the option list on Turn 2
            if (option_list_len_T2 > 1):                                           # -- if the option list has more than 1 option
                self.movesetT2[self.boardT2].remove(self.optionT2)                 # --- remove the option that resulted in a loss
            # if end
            
            if (self.optionT4):                                                    # - if there was a Turn 4 at all
                option_list_len_T4 = self.movesetT4[self.boardT4].__len__()        # -- check the length of the option list on Turn 4
                if (option_list_len_T4 > 1):                                       # -- if the option list has more than 1 option
                    self.movesetT4[self.boardT4].remove(self.optionT4)             # --- remove the option that resulted in a loss
                # if end
            # if end
            
            if (self.optionT6):                                                    # - if there was a Turn 6 at all
                option_list_len_T6 = self.movesetT4[self.boardT6].__len__()        # -- check the length of the option list on Turn 6
                if (option_list_len_T6 > 1):                                       # -- if the option list has more than 1 option
                    self.movesetT6[self.boardT6].remove(self.optionT6)             # --- remove the option that resulted in a loss
                # if end
            # #if end
        else:                                                                      # if the result given wasnt 'win' or 'loss'
            self.log.add('result unclear, cant learn.')                            # - log the issue
        # if end
        self.debug_log.add('Post-Learn:-----------')
        self.debug_log.add(self.movesetT2[self.boardT2])
        if (self.boardT4): self.debug_log.add(self.movesetT4[self.boardT4])
        if (self.boardT6): self.debug_log.add(self.movesetT6[self.boardT6])
        self.debug_log.add('----------------------')
        # no matter what, reset the board and option values so they cant carry over                                
        self.boardT2 = None
        self.optionT2 = None
        self.boardT4 = None
        self.optionT4 = None
        self.boardT6 = None
        self.optionT6 = None
    # learn end

    def take_turn(self, start, move):
        '''
        #* Make the move from starting position to move position.add().\n
        # @param start: Integer - The index of the tile that will be moving.\n
        # @param move: Integer - The index of the tile that will be moved to.
        '''
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
        self.boardT2 = board        
        self.optionT2 = self.get_options(board, self.movesetT2)
        start_pos = self.optionT2[0]
        move_pos = self.optionT2[1]
        self.take_turn(start_pos, move_pos)
        
        self.debug_log.add('After Turn 2\nself.boardT2: %s\nself.optionT2: %s\n\n'%(self.boardT2, self.optionT2))
        self.log.add('Turn 2: Computer moves from position %s to %s'%(start_pos, move_pos))
    # turn2 end

    def turn4(self):
        state = self.gb.get_game_state()
        board01 = [-1,  0, -1, -1,  1,  0,  0,  0,  1]
        board02 = [-1,  0, -1,  0,  1, -1,  1,  0,  0]
        board03 = [ 0, -1, -1,  1, -1,  0,  0,  0,  1]
        board04 = [-1, -1,  0,  0, -1,  1,  1,  0,  0]
        board05 = [-1,  0, -1,  1,  1,  0,  0,  1,  0]
        board06 = [-1,  0, -1,  0,  1,  1,  0,  1,  0]
        board07 = [-1, -1,  0,  1,  0,  1,  0,  0,  1]
        board08 = [ 0, -1, -1,  1,  0,  1,  0,  0,  1]
        board09 = [-1, -1,  0,  1,  0,  1,  1,  0,  0]
        board10 = [ 0, -1, -1,  1,  0,  1,  1,  0,  0]
        board11 = [ 0, -1, -1,  0, -1,  1,  1,  0,  0]
        board12 = [-1, -1,  0,  1, -1,  0,  0,  0,  1]
        board13 = [ 0, -1, -1, -1,  1,  1,  1,  0,  0]
        board14 = [-1,  0, -1, -1,  0,  1,  0,  1,  0]
        board15 = [-1,  0, -1,  1,  0, -1,  0,  1,  0]
        board16 = [-1, -1,  0,  1,  1, -1,  0,  0,  1]
        board17 = [ 0, -1, -1,  0,  1,  0,  0,  0,  1]
        board18 = [-1, -1,  0,  0,  1,  0,  1,  0,  0]
        board19 = [ 0, -1, -1,  0,  1,  0,  1,  0,  0]
        board20 = [-1, -1,  0,  0,  1,  0,  0,  0,  1]
        board21 = [-1,  0, -1,  1,  0,  0,  0,  0,  1]
        board22 = [-1,  0, -1,  0,  0,  1,  1,  0,  0]

        if (state == board01):
            board = 'board01'
        elif (state == board02):
            board = 'board02'
        elif (state == board03):
            board = 'board03'
        elif (state == board04):
            board = 'board04'
        elif (state == board05):
            board = 'board05'
        elif (state == board06):
            board = 'board06'
        elif (state == board07):
            board = 'board07'
        elif (state == board08):
            board = 'board08'
        elif (state == board09):
            board = 'board09'
        elif (state == board10):
            board = 'board10'
        elif (state == board11):
            board = 'board11'
        elif (state == board12):
            board = 'board12'
        elif (state == board13):
            board = 'board13'
        elif (state == board14):
            board = 'board14'
        elif (state == board15):
            board = 'board15'
        elif (state == board16):
            board = 'board16'
        elif (state == board17):
            board = 'board17'
        elif (state == board18):
            board = 'board18'
        elif (state == board19):
            board = 'board19'
        elif (state == board20):
            board = 'board20'
        elif (state == board21):
            board = 'board21'
        elif (state == board22):
            board = 'board22'
        else:
            msg = 'uh oh! bad board state %s'%(state)
            self.log.add(msg)
            self.debug_log.add(msg)
            return
        # if end
        self.boardT4 = board
        self.optionT4 = self.get_options(board, self.movesetT4)
        start_pos = self.optionT4[0]
        move_pos = self.optionT4[1]
        self.take_turn(start_pos, move_pos)
        
        self.log.add('Turn 4: Computer moves from position %s to %s'%(start_pos, move_pos))
    # turn4 end

    def turn6(self):
        state = self.gb.get_game_state()
        board01 = [ 0,  0, -1, -1, -1,  1,  0,  0,  0]
        board02 = [-1,  0,  0,  1, -1, -1,  0,  0,  0]
        board03 = [-1,  0,  0,  1,  1,  1,  0,  0,  0]
        board04 = [ 0,  0, -1,  1,  1,  1,  0,  0,  0]
        board05 = [ 0, -1,  0, -1,  1,  1,  0,  0,  0]
        board06 = [ 0, -1,  0,  1,  1, -1,  0,  0,  0]
        board07 = [-1,  0,  0, -1, -1,  1,  0,  0,  0]
        board08 = [ 0,  0, -1,  1, -1, -1,  0,  0,  0]
        board09 = [ 0,  0, -1, -1,  1,  0,  0,  0,  0]
        board10 = [-1,  0,  0,  0,  1, -1,  0,  0,  0]
        board11 = [ 0, -1,  0,  1, -1,  0,  0,  0,  0]
        board12 = [ 0, -1,  0,  0, -1,  1,  0,  0,  0]
        board13 = [-1,  0,  0, -1,  1,  0,  0,  0,  0]
        board14 = [ 0,  0, -1,  0,  1, -1,  0,  0,  0]

        if (state == board01):
            board = 'board01'
        elif (state == board02):
            board = 'board02'
        elif (state == board03):
            board = 'board03'
        elif (state == board04):
            board = 'board04'
        elif (state == board05):
            board = 'board05'
        elif (state == board06):
            board = 'board06'
        elif (state == board07):
            board = 'board07'
        elif (state == board08):
            board = 'board08'
        elif (state == board09):
            board = 'board09'
        elif (state == board10):
            board = 'board10'
        elif (state == board11):
            board = 'board11'
        elif (state == board12):
            board = 'board12'
        elif (state == board13):
            board = 'board13'
        elif (state == board14):
            board = 'board14'
        else:
            msg = 'uh oh! bad board state %s'%(state)
            self.log.add(msg)
            self.debug_log.add(msg)
            return
        # if end
        self.boardT6 = board
        self.optionT6 = self.get_options(board, self.movesetT6)
        start_pos = self.optionT6[0]
        move_pos = self.optionT6[1]
        self.take_turn(start_pos, move_pos)
        
        self.log.add('Turn 6: Computer moves from position %s to %s'%(start_pos, move_pos))
    # turn6 end
# class end