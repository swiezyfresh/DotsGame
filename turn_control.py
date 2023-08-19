import checker_control as checker_c
import player_control as player_c
import board_control as board_c

class Turn:

    def __init__(self, turn_owner, turn_count, win_line):
        self.turn_count = turn_count
        self.turn_owner = turn_owner
        self.turn_checker_sign = self.turn_owner.checker_sign
        self.win_line = win_line 
    
    def start_turn(self):
        print("TURN {} | PLAYER {} | CHECKER SIGN {}".format(self.turn_count, self.turn_owner, self.turn_checker_sign))
    
    def place_checker(self, board):
        checker = checker_c.Checker(self.turn_owner)
        checker.choose_x(board)
        checker.choose_y(board)
        return checker
    
    def check_horizontal_status(self, board):
        for row_index in range(1, board.rows):
            print("CHECKED ROW:", str(row_index))
            column_index = 1
            #for column_index in range(1, 5):
            while column_index + self.win_line - 1 < board.columns:
                if board.board_array[column_index][row_index] == self.turn_checker_sign:
                    checked_fields = 0
                    print("CHECKED FIELD NOTICED checking from COLUMNS:", str(column_index), "to:",str(column_index+3))
                    for checked_column_index in range(column_index, column_index+self.win_line):
                        if board.board_array[checked_column_index][row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    print("CHECKED FIELDS COUNTER in this range:", str(checked_fields))
                    if checked_fields == self.win_line:
                        return True
                column_index += 1
            row_index += 1
        return False
    
    def check_vertical_status(self, board):
        for column_index in range(1, board.columns):
            #print("CHECKED COLUMN:", str(column_index))'
            #for row_index in range(1, 4):
            row_index = 1
            while row_index + self.win_line - 1 < board.rows:
                if board.board_array[column_index][row_index] == self.turn_checker_sign:
                    checked_fields = 0
                    #print("CHECKED FIELD NOTICED checking from ROWS:", str(row_index), "to:",str(row_index+3))
                    for checked_row_index in range(row_index, row_index+self.win_line):
                        if board.board_array[column_index][checked_row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    #print("CHECKED FIELDS COUNTER in this range:", str(checked_fields))
                    if checked_fields == self.win_line:
                        return True
                row_index += 1
            column_index += 1
        return False
    
    def check_diagonally_down_status(self, board):
        start_row_index = 1
        board_array = board.board_array
        while start_row_index + self.win_line - 1 < board.rows:
            start_col_index = 1
            while start_col_index + self.win_line - 1 < board.columns:
                if board_array[start_col_index][start_row_index] == self.turn_checker_sign:
                    print("I SEE A CHECKER, I WILL CHECK THIS DIAGONAL")
                    checked_fields = 0
                    for checked_col_index, checked_row_index in zip(range(start_col_index, start_col_index + self.win_line), range(start_row_index, start_row_index + 4)):
                        print("CHECKING " + str(checked_col_index) +":"+ str(checked_row_index))
                        if board_array[checked_col_index][checked_row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    if checked_fields == self.win_line:
                        return True
                start_col_index += 1
            start_row_index += 1
        return False

    def check_diagonally_up_status(self, board):
        start_row_index = 1
        board_array = board.board_array
        while start_row_index + self.win_line - 1 < board.rows:
            start_col_index = board.columns - 1
            while start_col_index - self.win_line - 1 > 0:
                if board_array[start_col_index][start_row_index] == self.turn_checker_sign:
                    print("I SEE A CHECKER, I WILL CHECK THIS DIAGONAL")
                    checked_fields = 0
                    for checked_col_index, checked_row_index in zip(range(start_col_index, start_col_index - self.win_line, -1), range(start_row_index, start_row_index + 4)):
                        print("CHECKING " + str(checked_col_index) +":"+ str(checked_row_index))
                        if board_array[checked_col_index][checked_row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    if checked_fields == self.win_line:
                        return True
                start_col_index -= 1
            start_row_index += 1
        return False

    def check_win_status(self, board):
        horizontal = self.check_horizontal_status(board)
        vertical = self.check_vertical_status(board)
        diagonally_down = self.check_diagonally_down_status(board)
        diagonally_up = self.check_diagonally_up_status(board)
        all = horizontal or vertical or diagonally_down or diagonally_up
        return all