from lab1 import BoardGame

if __name__ == "__main__":
    games = []
    
    game1 = BoardGame()
    game2 = BoardGame()
    
    game3 = BoardGame("Chess", 2, 2)
    game4 = BoardGame("Monopoly", 2, 4)
    
    game5 = BoardGame.get_instance()
    game6 = BoardGame.get_instance()
    
    games.extend([game1, game2, game3, game4, game5, game6])
    
    for id, value in enumerate(games):
        print(id, value)