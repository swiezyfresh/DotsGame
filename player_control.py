import random
import board_control as board_ctrl
import board_colors as board_colors

fg_colors = board_colors.colors.fg()
format_colors = board_colors.colors()

class Player:
    player_counter = 0
    def __init__(self):
        Player.player_counter += 1
        self.id = Player.player_counter
        self.name = "Player " + str(self.id)
        self.checker_sign = str(self.id)
        if self.id % 2 == 0:
            self.checker_color = board_colors.colors.fg.blue
        else:
            self.checker_color = board_colors.colors.fg.red
        self.order = random.random()

    def set_name(self):
        name = input("PLEASE ENTER YOUR NICKNAME: ")
        if len(name) > 30:
            print("NICKNAME MUST HAVE MAXIMUM 30 CHARACTERS!")
            self.set_name()
        self.name = name
    
    def set_checker_color(self):
        fg_colors = board_colors.colors.fg()
        print("AVAILABLE COLORS: ")        
        print(fg_colors.display_colors())
        color_choice = input("PLEASE ENTER YOUR CHECKER COLOR: ").lower()
        if hasattr(fg_colors, str(color_choice)):
            self.checker_color = getattr(fg_colors, color_choice)
            self.checker_color = self.checker_color
        else:
            print("TYPE IN EXACT COLOR NAME FROM THE LIST!")
            self.set_checker_color()
            return

    def set_checker_sign(self, board):
        sign = input("PLEASE ENTER YOUR CHECKER SIGN: " + self.checker_color + format_colors.reset)
        if len(sign) > 1:
            print("CHECKER SIGN MUST BE A SINGLE CHARACTER!")
            self.set_checker_sign(board)
        elif sign == board.empty_sign:
            print("CHECKER SIGN MUST BE DIFFERENT FROM EMPTY SIGN!")
            self.set_checker_sign(board)
        else:
            self.checker_sign = format_colors.bold + self.checker_color + sign + format_colors.reset

    def __repr__(self):
        return self.name