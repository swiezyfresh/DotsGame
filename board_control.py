from string import ascii_uppercase as auc
class Board:
    board_counter = 0
    
    def __init__(self, columns=7, rows=6, empty_sign="O"):
        self.board_id = Board.board_counter
        Board.board_counter += 1
        self.columns = columns
        self.rows = rows
        self.empty_sign = empty_sign
        self.board_array = []
        self.board_display = ""
        self.setup_board_fields()
    
    def __repr__(self):
        self.refresh_board()
        return self.board_display
    
    # Define initial empty board by placing empty field signs
    def setup_board_fields(self):
        # Iterate through each column of the board
        for column in range(self.columns):
            # Place empty field signs in a row sub-array of iterated column  
            column = [self.empty_sign for row in range(self.rows)]
            # Append this column to the board array
            self.board_array.append(column)

    # Define headers for first row (column headers) and first column (row headers)
    def setup_board_headers(self):
        # Define empty lists of headers
        column_headers = []
        row_headers = []
        # Iterate through each column and add its ASCII uppercase alphabetic representation (auc_repr) to column headers list
        for column in range(self.columns):
            auc_repr = auc[column]
            column_headers.append(auc_repr)
        # Iterate through each row and add its numeric representation (num_repr) incremented by 1 (because 0-indexing) to row headers list
        for row in range(self.rows):
            num_repr = str(row+1)
            row_headers.append(num_repr)
        
        # The first upper-left element of the board has to be an empty diagonal division \ between columns and rows headers
        row_headers.insert(0, '\\')
        # Increment the columns and raws parameter (so length for 2d board array ->[+1]->[+1])
        self.columns += 1
        self.rows += 1
        return column_headers, row_headers

    # Place headers for rows and columns into the board array
    def setup_board_connect(self, column_headers, row_headers):
        column_index = 0
        # Iterate through each column and add the corresponding column header at the first row of column (index 0)
        for column in self.board_array:
            column.insert(0, column_headers[column_index])
            column_index += 1
        # Add a seperate column containing corresponding row headers as a first column (index 0)
        self.board_array.insert(0,row_headers)

    # Prepare a string representation of the board array to be displayed as a board for the user
    def setup_board_display(self):
        board_display = ""
        # Loop for X times (X - the length of board rows)
        for row_index in range(self.rows):
            row_display = ""
            # Iterate through each column the row passes through and save the value of the array at a given row and column
            for column_index in range(self.columns):
                row_display += str(self.board_array[column_index][row_index]) + " "
            # Add board array list elements to a temporary string representation of each row of the 2d array [][]<-
            board_display += row_display + "\n"
        return board_display
    
    # Initialize the board by generating empty fields, adding rows and connecting them
    def generate_board(self):
        column_headers, row_headers = self.setup_board_headers()
        self.setup_board_connect(column_headers, row_headers)
        self.board_display = self.setup_board_display()
    
    # Add a new checker to the board
    def add_checker(self, x_pos, y_pos, sign):
        self.board_array[x_pos][y_pos] = sign

    # Refresh the board after a checker was placed
    def refresh_board(self):
        self.board_display = self.setup_board_display()
        print("===============")
        print(self.board_display)
        print("===============")