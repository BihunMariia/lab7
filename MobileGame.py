from game import Game

class MobileGame(Game):
    def __init__(self, producer, title, year_of_release, min_age):
        super().__init__(producer, title, year_of_release, 1, 1)
        self.min_age = min_age

    def get_top_players(self):
        return ("nOnO", "Natus Vincere")
                
    def __str__(self):
        return f"{super().__str__()}\nMin Age: {self.min_age}"

    def add_player(self):
        pass
    
    def remove_player(self):
        pass
