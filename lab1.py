class BoardGame:
    def __init__(self, title, minPlayers, maxPlayers):
        self.title = title
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.currentPlayers = 0

    def addPlayer(self):
        if self.currentPlayers < self.maxPlayers:
            self.currentPlayers += 1
            print("Гравець доданий.")
        else:
            print("Досягнуто максимальну кількість гравців.")

    def removePlayer(self):
        if self.currentPlayers > 0:
            self.currentPlayers -= 1
            print("Гравець видалений.")
        else:
            print("Немає гравців у грі.")

    def canPlay(self):
        return self.currentPlayers >= self.minPlayers



game = BoardGame("Назва гри", 2, 4)
print(game.canPlay()) 

game.addPlayer()  
game.addPlayer()  
game.addPlayer()  
print(game.canPlay())  

game.removePlayer()  
game.removePlayer()  
game.removePlayer()  
print(game.canPlay())  
