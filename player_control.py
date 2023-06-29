import random
import board_control as board_c
class Player:
    player_counter = 0
    def __init__(self):
        Player.player_counter += 1
        self.id = Player.player_counter
        self.name = "Player " + str(self.id)
        self.checker_sign = str(self.id)
        self.order = random.random()

    def set_name(self):
        name = input("PLEASE ENTER YOUR NICKNAME: ")
        if len(name) > 30:
            print("NICKNAME MUST HAVE MAXIMUM 30 CHARACTERS!")
            self.set_name()
        self.name = name

    def set_checker_sign(self, board):
        sign = input("PLEASE ENTER YOUR CHECKER SIGN: ")
        if len(sign) > 1:
            print("CHECKER SIGN MUST BE A SINGLE CHARACTER!")
            self.set_checker_sign(board)
        elif sign == board.empty_sign:
            print("CHECKER SIGN MUST BE DIFFERENT FROM EMPTY SIGN!")
            self.set_checker_sign(board)
        else:
            self.checker_sign = sign

    def __repr__(self):
        return self.name