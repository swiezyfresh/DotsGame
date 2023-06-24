from string import ascii_uppercase as auc
class Board:
    board_counter = 0
    def __init__(self, columns=7, rows=6, empty_field_marker="O", checked_field_marker="X"):
        Board.board_counter += 1
        self.board_id = Board.board_counter
        self.columns = columns
        self.rows = rows
        self.empty_field_marker = empty_field_marker
        self.checked_field_marker = checked_field_marker
        self.board_array = []

    def board_fields_setup(self):
        for column in range(self.columns):
            column = [self.empty_field_marker for row in range(self.rows)]
            self.board_array.append(column)
        print(self.board_array)

    def board_headers_setup(self):
        column_headers = ""
        row_headers = ""
        for column in range(self.columns):
            column_headers += auc[column]
        for row in range(self.rows):
            row_headers += str(row+1)
        return column_headers, row_headers

new_board = Board()
new_board.board_fields_setup()
print(new_board.board_headers_setup())
