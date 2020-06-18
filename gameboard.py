class GameBoard():
    def __init__(self):
        self.row_top = [-1, -1, -1]
        self.row_mid = [0, 0, 0]
        self.row_bot = [1, 1, 1]
    # __init__ end

    def get_top_row(self):
        return self.row_top
    # get_top_row

    def get_mid_row(self):
        return self.row_mid
    # get_mid_row

    def get_bot_row(self):
        return self.row_bot
    # get_bot_row

    def check_player_win(self):
        if (1 in self.row_top):
            return True
        # if end
        return False
    # #check_player_win
    
    def check_computer_win(self):
        if (-1 in self.row_bot):
            return True
        # if end
        return False
    # #check_computer_win
# class end