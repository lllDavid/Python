class game:
    def __init__(self):
        self.game = input("Game: ")
        self.herausgeber = input("Herausgeber: ")

    def ausgabe(self):
        print(f"Lieblingsspiel {self.game} und Herausgeber {self.herausgeber}")

game = game()
game.ausgabe()