from game import Game
from board_game import BoardGame
from ComputerGame import ComputerGame
from MobileGame import MobileGame
from PlayStationGame import PlayStationGame

class GameManager:
    def __init__(self):
        self.game_list = []

    def add_game(self, game: Game):
        self.game_list.append(game)

    def find_games_with_more_than_five_max_players(self) -> list[Game]:
        return [game.title for game in self.game_list if game.max_players > 5]

    def find_games_with_min_players_equals_two(self) -> list[Game]:
        return [game for game in self.game_list if game.min_players == 2]

    def __str__(self):
        games_str = '\n'.join(f"{index}. {game}" for index, game in enumerate(self.game_list, 1))
        return f"Games:\n{games_str}"
    
    def __len__(self):
        return len(self.game_list)

    def __getitem__(self, index):
        return self.game_list[index]

    def __iter__(self):
        return iter(self.game_list)

    #def add_players_for_all_games(self):
   #     return [item.add_player() for item in self.game_list]

    def add_players_for_all_games(self):
        return [f"{game} - {result}" for game, result in zip(self.game_list, [item.add_player() for item in self.game_list])]

    def check_conditions(game_manager):
        result = {}
        result["all"] = all(game.year_of_release > 1900 for game in game_manager.game_list)
        result["any"] = any(game.year_of_release < 1920 for game in game_manager.game_list)
        return result

if __name__ == "__main__":
    game_manager = GameManager()

    game_manager.add_game(BoardGame("Hasbro", "Monopolia", 1935, 2, 6))
    game_manager.add_game(BoardGame("Dimitry Davidoff", "Mafia", 1986, 4, 16))
    game_manager.add_game(ComputerGame( "Valve Corporation", "Counter-Strike", 2012, "PC"))
    game_manager.add_game(MobileGame("Activision Publishing", "Call Of Duty", 2023, 16))
    game_manager.add_game(PlayStationGame("Sony Interactive Entertainment", "Horizon Forbidden West", 2022,"action"))
    
    print(game_manager.check_conditions())
    game = BoardGame("Hasbro", "Monopolia", 1935, 2, 6)
    int_attributes = game.filter_attributes_by_type(int)
    print(int_attributes)

    print(game_manager.add_players_for_all_games())
    print(game_manager)
    print("\nGames with more than five max players:\n")
    print(game_manager.find_games_with_more_than_five_max_players())
    print("\nGames with min players equals two:\n")
    print(game_manager.find_games_with_min_players_equals_two())
