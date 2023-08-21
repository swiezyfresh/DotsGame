import board_control as board_c
import random

test_board = board_c.Board(4,4)
test_board.setup_board_fields()
test_board.generate_board()
test_win_line = 3

def setup_coordinates(x1, y1, x2, y2):
    return {
                "x1" : x1,
                "y1" : y1,
                "x2" : x2,
                "y2" : y2
            }

def generate_vertical_set():
    vertical_set = []
    for x in range(1, test_board.columns):
        for y in range(1, test_board.rows):
            y_upper = y
            y_lower = y_upper + test_win_line - 1
            line_length = y_lower - y_upper + 1
            if y_upper + line_length <= test_board.rows and line_length == test_win_line:
                line_cords = setup_coordinates(x, y_upper, x, y_lower)
                vertical_set.append(line_cords)
            else: 
                pass
    return vertical_set

def generate_horizontal_set():
    horizontal_set = []
    for y in range(1, test_board.rows):
        for x in range(1, test_board.columns):
            x_left = x
            x_right = x_left + test_win_line - 1
            line_length = x_right - x_left + 1
            if x_left + line_length <= test_board.columns and line_length == test_win_line:
                line_cords = setup_coordinates(x_left, y, x_right, y)
                horizontal_set.append(line_cords)
            else: 
                pass
    return horizontal_set

def generate_diagonally_up_set():
    du_set = []
    x_left = 1
    x_right = x_left + test_win_line - 1
    while x_right < test_board.columns:
        y_left = 1
        y_right = y_left + test_win_line - 1
        while y_right < test_board.rows:
            line_cords = setup_coordinates(x_left, y_left, x_right, y_right)
            print(line_cords)
            du_set.append(line_cords)
            y_left += 1
            y_right += 1
        x_left += 1
        x_right += 1
    return du_set

def generate_diagonally_down_set():
    dd_set = []
    x_right = test_board.columns-1
    x_left = x_right - test_win_line + 1
    while x_left > 0:
        y_right = 1
        y_left = y_right + test_win_line - 1
        while y_left < test_board.rows:
            line_cords = setup_coordinates(x_left, y_left, x_right, y_right)
            print(line_cords)
            dd_set.append(line_cords)
            y_left += 1
            y_right += 1
        x_left -= 1
        x_right -= 1
    return dd_set
            
def choose_r_win_line(set):
    random_win_line = random.randrange(0,len(set),1)
    return set[random_win_line]

# def seperate_coordinates(line):
#     line_cords = list(line.values())
#     x1 = line_cords[0]
#     y1 = line_cords[1]
#     x2 = line_cords[2]
#     y2 = line_cords[3]
#     return {"x1": c_main, "higher": c_higher, "lower": c_lower}

def place_r_win_line(line_cords, set_type, sign):
    start_cord = None
    end_cord = None
    static_cord = None
    start_diagonal_cords = None
    end_diagonal_cords = None

    if set_type == "horizontal":
        start_cord = line_cords["x1"]
        end_cord = line_cords["x2"]
        static_cord = line_cords["y1"]
    elif set_type == "vertical":
        start_cord = line_cords["y1"]
        end_cord = line_cords["y2"]
        static_cord = line_cords["x1"]

    if set_type == "horizontal" or set_type == "vertical":  
        for i in range(start_cord, end_cord + 1):
            if set_type == "horizontal":
                test_board.add_checker(i, static_cord, sign)
            elif set_type == "vertical":
                test_board.add_checker(static_cord, i, sign)
        return

    if set_type == "diagonally_up":
        start_diagonal_cords = (line_cords["x1"], line_cords["y1"])
        end_diagonal_cords = (line_cords["x2"], line_cords["y2"])    
        j = 0
        for i in range(start_diagonal_cords[0], end_diagonal_cords[0] + 1):
            test_board.add_checker(start_diagonal_cords[0] + j, start_diagonal_cords[1] + j, sign)
            j += 1
    
    return

# Uncomment code lines with type of set you want to generate a test random win line      
 
# set = generate_horizontal_set()
# set_type = "horizontal"

# set = generate_vertical_set()
# set_type = "vertical"

# set = generate_diagonally_down_set()
# set_type = "diagonally_down"

# set = generate_diagonally_up_set()
# set_type = "diagonally_up"

#print(set)

# Choose a random line from the set and place it on the board
r_win_line = choose_r_win_line(set)
#r_win_line_cords = seperate_coordinates(r_win_line)
place_r_win_line(r_win_line, set_type, "X")

# Display the board with a random win line placed
test_board.refresh_board()
