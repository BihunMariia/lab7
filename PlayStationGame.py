from game import Game

class PlayStationGame(Game):
    def __init__(self, producer, title, year_of_release, genre):
        super().__init__(producer, title, year_of_release, 1, 1)
        self.genre = genre

    def get_top_players(self):
        return ("ZywOo", "KRiMZ")
    
    def __str__(self):
        return f"{super().__str__()}\nGenre: {self.genre}"

    def add_player(self):
        pass
    
    def remove_player(self):
        pass
