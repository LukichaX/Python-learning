class Player:
    def __init__(self, username, score):
        self.username = username
        self.score = score

    def add_score(self, points):
        self.score += points
        return print(self.score)

player1 = Player("LukichaX", 1000)

player1.add_score(500)