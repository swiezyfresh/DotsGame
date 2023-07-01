import checker_control as checker_c
import player_control as player_c
import board_control as board_c

class Turn:

    def __init__(self, turn_owner, turn_count):
        self.turn_count = turn_count
        self.turn_owner = turn_owner
        self.turn_checker_sign = self.turn_owner.checker_sign
    
    def start_turn(self):
        print("TURN {} | PLAYER {} | CHECKER SIGN {}".format(self.turn_count, self.turn_owner, self.turn_checker_sign))
    
    def place_checker(self, board):
        checker = checker_c.Checker(self.turn_owner)
        checker.choose_x(board)
        checker.choose_y(board)
        return checker
    
    def check_horizontal_status(self, board):
        for row_index in range(1, board.rows):
            #print("CHECKED ROW:", str(row_index))
            for column_index in range(1, 5):
                if board.board_array[column_index][row_index] == self.turn_checker_sign:
                    checked_fields = 0
                    #print("CHECKED FIELD NOTICED checking from COLUMNS:", str(column_index), "to:",str(column_index+3))
                    for checked_column_index in range(column_index, column_index+4):
                        if board.board_array[checked_column_index][row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    #print("CHECKED FIELDS COUNTER in this range:", str(checked_fields))
                    if checked_fields == 4:
                        return True
                column_index += 1
            row_index += 1
        return False
    
    def check_vertical_status(self, board):
        for column_index in range(1, board.columns):
            #print("CHECKED COLUMN:", str(column_index))
            for row_index in range(1, 4):
                if board.board_array[column_index][row_index] == self.turn_checker_sign:
                    checked_fields = 0
                    #print("CHECKED FIELD NOTICED checking from ROWS:", str(row_index), "to:",str(row_index+3))
                    for checked_row_index in range(row_index, row_index+4):
                        if board.board_array[column_index][checked_row_index] == self.turn_checker_sign:
                            checked_fields += 1
                    #print("CHECKED FIELDS COUNTER in this range:", str(checked_fields))
                    if checked_fields == 4:
                        return True
                row_index += 1
            column_index += 1
        return False
