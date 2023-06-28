from game import Game
from exceptions import InvalidPlayersNumber
from logged import logged

class BoardGame(Game):
    def __init__(self, producer, title, year_of_release, min_players, max_players, instruments):
        super().__init__(producer, title, year_of_release, min_players, max_players)
        self.instruments = instruments

    @logged(InvalidPlayersNumber, "console")
    def add_player(self):
        if self.current_players < self.max_players:
            self.current_players += 1
            print("Player added.")
        else:
            raise InvalidPlayersNumber("The maximum number of players has been reached.")

        return self.current_players

    def remove_player(self):
        if self.current_players > self.min_players:
            self.current_players -= 1
            print("Player removed.")
        else:
            print("The minimum number of players has been reached.")

    default_board_game = None

    def filter_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __str__(self):
        return f"{super().__str__()}\nInstruments: {self.instruments}"

    @staticmethod
    def get_instance():
        if BoardGame.default_board_game is None:
            BoardGame.default_board_game = BoardGame()
        return BoardGame.default_board_game

    def get_top_players(self):
        return ("Ян-Уве Вальднер", "Маґнус Карлсен")
