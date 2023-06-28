from abc import ABC, abstractmethod

class Game(ABC):
    def __init__ (self, producer,title, year_of_release, min_players, max_players):
        self.producer = producer
        self.title = title
        self.year_of_release = year_of_release
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = 0

    def __str__(self):
        return f"Game: {self.title}\nProducer: {self.producer}\nYear of Release: {self.year_of_release}\nMin Players:{self.min_players}\nMax Players: {self.max_players}\nCurrent Players: {self.current_players}"
    
    @abstractmethod
    def add_player(self):
        pass

    @abstractmethod
    def remove_player(self):
        pass
