from game import Game

class BoardGame(Game):
    def __init__(self, producer, title, year_of_release, min_players, max_players):
        super().__init__(producer, title, year_of_release, min_players, max_players)

    def add_player(self):
        if self.current_players < self.max_players:
            self.current_players += 1
            print("Player added.")
        else:
            print("The maximum number of players has been reached.")
    
    def remove_player(self):
        if self.current_players > self.min_players:
            self.current_players -= 1
            print("Player removed.")
        else:
            print("The minimum number of players has been reached.")

    default_board_game = None

    def __str__(self):
        return f"{super().__str__()}\nBoard Game Specific Attribute: <Specify the attribute here>"

    @staticmethod
    def get_instance():
        if BoardGame.default_board_game is None:
            BoardGame.default_board_game = BoardGame()
        return BoardGame.default_board_game


