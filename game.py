from abc import ABC, abstractmethod

class Game:
    def __init__ (self, producer,title, year_of_release : int, min_players, max_players):
        self.producer = producer
        self.title = title
        self.year_of_release = year_of_release
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = 4
        self.top_players = set()

    @abstractmethod
    def get_top_players(self):
        pass

    def __iter__(self):
        return iter(self.top_players_set)

    def __str__(self):
        return f"Game Title: {self.title}\nYear of Release: {self.year_of_release}\nMin Players: {self.min_players}\nMax Players: {self.max_players}\nCurrent Players: {self.current_players}"

    @abstractmethod
    def add_player(self):
        pass

    @abstractmethod
    def remove_player(self):
        pass
