import board_control as board_c
from string import ascii_uppercase as auc
class Checker:
    checker_count = 0

    def __init__(self, player):
        self.x_pos = None
        self.y_pos = None
        self.owner = player
        self.sign = player.checker_sign

    def __repr__(self):
        return self.sign
    
    # Define the x position (column) where checker will be dropped
    def choose_x(self, board):
        # Choose the x position (column) for checker drop
        x_pos = input("DROP CHECKER TO COLUMN (A-G): ").upper()
        # Calculate x position index for the board array
        # The index is calculated based on x_pos character position in ASCII uppercase alphabet (A=0, B=1 etc.)
        auc_index = auc.index(x_pos)
        # Then auc_index modulo by the length of the board array
        # It has to be incremented by 1 to avoid the first header element in x_position (column) list 
        self.x_pos = auc_index % len(board.board_array) + 1
        # Set x_pos of Checker instance to the result of the calculation

    # Define the y position (row) where checker will land
    def choose_y(self, board):
        # Get the y_position (row) sub-array of specific x_position (column) for the board_array
        column = board.board_array[self.x_pos]
        # Iterate through column's rows from index 1 (avoid the header) of row sub-array
        for index in range(1,len(column)):
            row = column[index]
            # If a earlier-placed checker is found in the sub-array, we place the new checker aboce it (index-1)
            if row != board.empty_sign:
                self.y_pos = index-1
                return
        #If no earlier-placed checker was found in the sub-array, we place the new_checker at last possible y_pos
        self.y_pos = len(column)-1

new_board = board_c.Board()
new_board.generate_board()

#new_checker = Checker(player="Ja")
#new_checker.choose_x(new_board)
#new_checker.choose_y(new_board)
#print(new_checker.y_pos)