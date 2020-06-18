import gameboard

class Pawn():
    def __init__(self, owner: int, space: int, gameboard: gameboard.GameBoard):
        '''
        #* The pawn object that is placed on the board.\n
        # @param owner: int - The owner of the pawn, 1 for player or -1 for computer.\n
        # @param space: Int - The space the pawn occupies on the board.
        '''
        self.owner = owner
        self.space = space
        self.gameboard = gameboard
        self.moves = {'left': False, 'forward': False, 'right': False}
    # __init__ end

    def get_moves(self):
        '''
        #* Return the moves available to the Pawn. If a move is invalid, the value will be None.
        '''
        pawn_col = self.space % 3                               # mod 3 to get pawn column
        print('pawn column %s'%(pawn_col))
        if (self.owner == 1):                            # if the pawn belongs to the player
            if (self.space > 5):                                # - if the pawn is in the bottom row
                next_row = self.gameboard.get_mid_row()         # -- get the middle row of the gameboard
                print('pawn column %s'%(next_row))
                if (pawn_col == 0): self.left_moves(next_row)   # -- if the pawn is on the left wall                    
                if (pawn_col == 1): self.center_moves(next_row) # -- if the pawn is the center                    
                if (pawn_col == 2): self.right_moves(next_row)  # -- if the pawn is on the right wall
            elif (self.space < 6 or self.space > 2):            # - if the pawn is in the mid row
                next_row = self.gameboard.get_top_row()         # -- get the middle row of the gameboard
                print('pawn column %s'%(next_row))
                if (pawn_col == 0): self.left_moves(next_row)   # -- if the pawn is on the left wall                    
                if (pawn_col == 1): self.center_moves(next_row) # -- if the pawn is the center                    
                if (pawn_col == 2): self.right_moves(next_row)  # -- if the pawn is on the right wall
            else: pass
        elif (self.owner == -1):
            if (self.space < 3):                                # - if the pawn is in the top row
                next_row = self.gameboard.get_mid_row()         # -- get the middle row of the gameboard
                print('pawn column %s'%(next_row))
                if (pawn_col == 0): self.left_moves(next_row)   # -- if the pawn is on the left wall                    
                if (pawn_col == 1): self.center_moves(next_row) # -- if the pawn is the center                    
                if (pawn_col == 2): self.right_moves(next_row)  # -- if the pawn is on the right wall
            elif (self.space < 6 or self.space > 2):            # - if the pawn is in the mid row
                next_row = self.gameboard.get_bot_row()         # -- get the middle row of the gameboard
                print('pawn column %s'%(next_row))
                if (pawn_col == 0): self.left_moves(next_row)   # -- if the pawn is on the left wall                    
                if (pawn_col == 1): self.center_moves(next_row) # -- if the pawn is the center                    
                if (pawn_col == 2): self.right_moves(next_row)  # -- if the pawn is on the right wall
            else: pass
        else: pass
        return self.moves
    # get_moves end

    def left_moves(self, next_row):
        if (next_row[0] == 0): self.moves.update({'forward': True})    # if the next row is empty move forward is okay
        
        if (self.owner == 1):                                          # if the owner is the player
            if (next_row[1] == -1): self.moves.update({'right': True}) # - if the top right tile is an enemy, attack is okay
        else:                                                          # if the owner is the computer
            if (next_row[1] == 1): self.moves.update({'right': True})  # - if the bottom right tile is an enemy, attack is okay
        # if end
    # left_moves end

    def center_moves(self, next_row):
        if (next_row[1] == 0): self.moves.update({'forward': True})    # if the next row is empty move forward is okay

        if (self.owner == 1):                                          # if the owner is the player
            if (next_row[0] == -1): self.moves.update({'left': True})  # - if the top left tile is an enemy, attack is okay
            if (next_row[2] == -1): self.moves.update({'right': True}) # - if the top right tile is an enemy, attack is okay
        else:                                                          # if the owner is the computer
            if (next_row[0] == 1): self.moves.update({'left': True})   # - if the bottom left tile is an enemy, attack is okay
            if (next_row[2] == 1): self.moves.update({'right': True})  # - if the bottom right tile is an enemy, attack is okay
        # if end
    # center_moves end

    def right_moves(self, next_row):
        if (next_row[2] == 0): self.moves.update({'forward': True})    # if the next row is empty move forward is okay
        
        if (self.owner == 1):                                          # if the owner is the player
            if (next_row[1] == -1): self.moves.update({'left': True})  # - if the top left tile is an enemy, attack is okay
        else:                                                          # if the owner is the computer
            if (next_row[1] == 1): self.moves.update({'left': True})   # - if the bottom left tile is an enemy, attack is okay
        # if end
    # right_moves end

    def get_space(self):
        return self.space
    # get_space end
# class end