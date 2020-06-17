class GameBoard():
    def __init__(self):
        self.row_top = ['Computer', 'Computer', 'Computer']
        self.row_mid = ['', '', '']
        self.row_bot = ['Player', 'Player', 'Player']
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
        if ('Player' in self.row_top):
            return True
        # if end
        return False
    # #check_player_win
    
    def check_computer_win(self):
        if ('Computer' in self.row_bot):
            return True
        # if end
        return False
    # #check_computer_win
# class end