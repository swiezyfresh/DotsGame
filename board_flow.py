from string import ascii_uppercase as auc
class Board:
    board_counter = 0
    
    def __init__(self, columns=7, rows=6, empty_field_marker="O"):
        self.board_id = Board.board_counter
        Board.board_counter += 1
        self.columns = columns
        self.rows = rows
        self.empty_field_marker = empty_field_marker
        self.board_array = []
        self.board_display = ""
        self.setup_board_fields()
    
    def __repr__(self):
        return self.board_display

    def setup_board_fields(self):
        for column in range(self.columns):
            column = [self.empty_field_marker for row in range(self.rows)]
            self.board_array.append(column)

    def setup_board_headers(self):
        column_headers = []
        row_headers = []
        for column in range(self.columns):
            column_headers.append(auc[column])
        for row in range(self.rows):
            row_headers.append(str(row+1))
        row_headers.insert(0, " ")
        self.columns += 1
        return column_headers, row_headers

    def setup_board_connect(self, column_headers, row_headers):
        column_index = 0
        for column in self.board_array:
            column.insert(0, column_headers[column_index])
            column_index += 1
        self.board_array.insert(0,row_headers)

    def setup_board_display(self):
        board_display = ""
        for row_index in range(self.rows):
            row_display = ""
            for column_index in range(self.columns):
                row_display += str(self.board_array[column_index][row_index]) + " "
            board_display += row_display + "\n"
        return board_display
    
    def generate_board(self):
        column_headers, row_headers = self.setup_board_headers()
        self.setup_board_connect(column_headers, row_headers)
        board_display = self.setup_board_display()
        self.board_display = board_display
        print(self.board_display)

new_board = Board()
new_board.generate_board()
