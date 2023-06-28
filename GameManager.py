from typing import List
from game import Game
from BoardGame import BoardGame
from ComputerGame import ComputerGame
from MobileGame import MobileGame
from PlayStationGame import PlayStationGame

class GameManager:
    def __init__(self):
        self.game_list = []

    def add_game(self, game: Game):
        self.game_list.append(game)

    def find_games_with_more_than_five_max_players(self) -> List[Game]:
        return [game for game in self.game_list if game.max_players > 5]

    def find_games_with_min_players_equals_two(self) -> List[Game]:
        return [game for game in self.game_list if game.min_players == 2]

    def __str__(self):
        games_str = '\n'.join(str(game) for game in self.game_list)
        return f"Games:\n{games_str}"

if __name__ == "__main__":
    game_manager = GameManager()

    game_manager.add_game(BoardGame("Hasbro", "Monopolia", 1935, 2, 6))
    game_manager.add_game(BoardGame("Dimitry Davidoff", "Mafia", 1986, 4, 16))
    game_manager.add_game(ComputerGame( "Valve Corporation", "Counter-Strike", 2012, "PC"))
    
    game_manager.add_game(MobileGame("Activision Publishing", "Call Of Duty", 2023, 16))
    game_manager.add_game(PlayStationGame("Sony Interactive Entertainment", "Horizon Forbidden West", 2022,"action"))

    print(game_manager)

    print("\nGames with more than five max players:\n")
    print(game_manager.find_games_with_more_than_five_max_players())

    print("\nGames with min players equals two:\n")
    print(game_manager.find_games_with_min_players_equals_two())
