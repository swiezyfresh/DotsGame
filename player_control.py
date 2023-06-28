import random
class Player:
    def __init__(self, name, checker_sign):
        self.name = name
        self.checker_sign = checker_sign
        self.order = 0

    def randomize_order(self):
        self.order = random.random()

new_player = Player("KSK", "X")
new_player.randomize_order()
print(new_player.order)