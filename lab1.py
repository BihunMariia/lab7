class BoardGame:
    def __init__(self, title="", minPlayers=0, maxPlayers=0):
        self.title = title
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.currentPlayers = 0

    def __str__(self):
        return f"MyClass instance, title: {self.title}, minPlayers: {self.minPlayers}, maxPlayers: {self.maxPlayers}"
    
    def add_player(self):
        if self.currentPlayers < self.maxPlayers:
            self.currentPlayers += 1
            print("Гравець доданий.")
        else:
            print("Досягнуто максимальну кількість гравців.")

    def remove_player(self):
        if self.currentPlayers > 0:
            self.currentPlayers -= 1
            print("Гравець видалений.")
        else:
            print("Немає гравців у грі.")

    def can_play(self):
        return self.currentPlayers >= self.minPlayers
    
    defaultBoardGame = None

    @staticmethod
    def getInstance():
        if BoardGame.defaultBoardGame is None:
            BoardGame.defaultBoardGame = BoardGame()
        return BoardGame.defaultBoardGame

