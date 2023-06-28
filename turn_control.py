import checker_control as checker_c
import player_control as player_c
import board_control as board_c

class Turn:

    def __init__(self, turn_owner, board):
        self.turn_number = 0
        self.turn_owner = turn_owner
        self.board = board
    
    def start_turn(self):
        self.turn_number += 1
        print("TURN {} | PLAYER {}".format(self.turn_number, self.turn_owner))
    
    def place_checker(self):
        checker = checker_c.Checker(self.turn_owner)
        checker.choose_x(self.board)
        checker.choose_y(self.board)
        return checker