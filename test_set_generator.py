import board_control as board_c

test_board = board_c.Board(5,5)
test_board.setup_board_fields()
test_board.generate_board()
test_win_line = 4

print(test_board.rows)
print(test_board.columns)

def generate_horizontal_wins():
    horizontal_set = []
    for x in range(1, test_board.columns):
        for y in range(1, test_board.rows):
            y_upper = y
            y_lower = y_upper + test_win_line - 1
            line_length = y_lower - y_upper + 1
            if y_upper + line_length <= test_board.rows and line_length == test_win_line:
                line_cords = {"x": x, "y_upper": y_upper, "y_lower": y_lower}
                horizontal_set.append(line_cords)
            else: 
                pass
    return horizontal_set

horizontal_set = generate_horizontal_wins()
print(horizontal_set)
                

#