from tile import Tile

class GameBoard():
    def __init__(self, buttons):
        self.tiles = []
        self.buttons = buttons

        self.new_board()
    # __init__ end

    def get_game_state(self):
        '''
        #* Get the current state of the board, showing who controls what.\n
        # @return List - The list of values of the controlled tiles.
        '''
        resp = []
        for tile in self.tiles:
            resp.append(tile.get_controlled())
        # for end
        return resp
    # get_game_state end

    def get_top_row(self):
        return [self.tiles[0], self.tiles[1], self.tiles[2]]
    # get_top_row

    def get_mid_row(self):
        return [self.tiles[3], self.tiles[4], self.tiles[5]]
    # get_mid_row

    def get_bot_row(self):
        return [self.tiles[6], self.tiles[7], self.tiles[8]]
    # get_bot_row

    def new_board(self):
        '''
        #* Create a new game board.
        '''
        for i in range(0, 9):
            tile = Tile(0, i, self.buttons[i])
            self.tiles.append(tile)
        # for end

        for i in range(0, 3):
            self.tiles[i].change_control(-1)
        # for end

        for i in range(6, 9):
            self.tiles[i].change_control(1)
        # for end
    # new_board end

    def reset_board(self):
        '''
        #* Set the game board to the default tile setup.
        '''
        for i in range(0, 3):
            self.tiles[i].change_control(-1)
        # for end
        for i in range(3, 6):
            self.tiles[i].change_control(0)
        # for end

        for i in range(6, 9):
            self.tiles[i].change_control(1)
        # for end
    # reset_board end

    def test_board(self):
        for i in range(0, 9):
            tile = Tile(0, i, self.buttons[i])
            self.tiles.append(tile)
        # for end

        for i in range(0, 3):
            self.tiles[i].change_control(-1)
        # for end

        self.tiles[5].change_control(-1)

        for i in range(6, 9):
            self.tiles[i].change_control(1)
        # for end
    # test_board end

    def show_moves(self, index):
        '''
        #* Show the moves of the given Tile index by recoloring the Tiles that can be reached by the selected Tile.\n
        # @param index: Integer - The Tile that is having it's moves shown.
        '''
        tile = self.tiles[index]
        column = index % 3
        row = int(index / 3)
        if (column == 0):
            self.show_move_forward(index)
            self.show_move_right(index)
        elif (column == 1):
            self.show_move_left(index)
            self.show_move_forward(index)
            self.show_move_right(index)
        else:
            self.show_move_left(index)
            self.show_move_forward(index)
        # if end
    # show_moves end

    def show_move_forward(self, index):
        forward_tile = self.tiles[index-3]
        if (forward_tile.get_controlled() == 0):
            forward_tile.style_button(forward_tile._style_movable)
    # show_move_forward end

    def show_move_left(self, index):
        left_tile = self.tiles[index-4]
        if (left_tile.get_controlled() == -1):
            left_tile.style_button(left_tile._style_attackable)
    # show_move_left end

    def show_move_right(self, index):
        right_tile = self.tiles[index-2]
        if (right_tile.get_controlled() == -1):
            right_tile.style_button(right_tile._style_attackable)
    # show_move_right end

    def unselect_all(self):
        '''
        #* Return all tiles to their default style.
        '''
        for tile in self.tiles:
            tile.style_button(tile._style_deselected)
        # for end
    # unselect_all end

    def __str__(self):
        resp = ''
        for tile in tiles:
            resp = '%s\n%s'%(resp, str(tile))
        # for end
        return resp
    # __str__ end
# class end