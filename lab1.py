class BoardGame:
    def __init__(self, title="", min_players=0, max_players=0):
        self.title = title
        self.min_players = min_players
        self.max_players = max_players
        self.current_players = 0

    def __str__(self):
        return f"MyClass instance, title: {self.title}, minPlayers: {self.min_players}, maxPlayers: {self.max_players}"
    
    def add_player(self):
        if self.current_players < self.max_players:
            self.current_players += 1
            print("Гравець доданий.")
        else:
            print("Досягнуто максимальну кількість гравців.")

    def remove_player(self):
        if self.current_players > 0:
            self.current_players -= 1
            print("Гравець видалений.")
        else:
            print("Немає гравців у грі.")

    def can_play(self):
        return self.current_players >= self.min_players
    
    default_board_game = None

    @staticmethod
    def get_instance():
        if BoardGame.default_board_game is None:
            BoardGame.default_board_game = BoardGame()
        return BoardGame.default_board_game


