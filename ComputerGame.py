from game import Game

class ComputerGame(Game):
    def __init__(self, producer, title, year_of_release, platform):
        super().__init__(producer, title, year_of_release, 1, 1)
        self.platform = platform

    def __str__(self):
        return f"{super().__str__()}\nPlatform: {self.platform}"

    def add_player(self):
        pass
    
    def remove_player(self):
        pass
