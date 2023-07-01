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
        board_length = len(board.board_array)
        # Choose the x position (column) for checker drop
        column_choice = input("DROP CHECKER TO COLUMN (A-G): ").upper()
        # First check if the input provided by the user is correct Type
        try:
            # Calculate x position index for the board array
            # The index is calculated based on x_pos character position in ASCII uppercase alphabet (A=0, B=1 etc.)
            auc_index = auc.index(column_choice)
        except ValueError:
            print("CHOOSE COLUMN BY ENTERING CORRESPONDING CHARACTER (A-G)!")
            self.choose_x(board)
            return
        if self.check_x(auc_index+1, board_length):
            self.choose_x(board)
            return
        else:
            # Then auc_index modulo by the length of the board array
            # It has to be incremented by 1 to avoid the first header element in x_position (column) list 
            x_pos = auc_index % board_length + 1
            self.x_pos = x_pos
            # Set x_pos of Checker instance to the result of the calculation

    # Support function to check if given x_pos corresponding column name fits in the board range
    def check_x(self, x_pos, length):
        if int(x_pos) >= length:
            print("CHOOSE COLUMN FROM GIVEN RANGE (A-G)!")
            return True
        return False
    
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