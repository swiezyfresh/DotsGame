import board_control as board_c
import random

test_board = board_c.Board(4,4)
test_board.setup_board_fields()
test_board.generate_board()
test_win_line = 3

def generate_horizontal_set():
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

def generate_vertical_set():
    vertical_set = []
    for y in range(1, test_board.rows):
        for x in range(1, test_board.columns):
            x_left = x
            x_right = x_left + test_win_line - 1
            line_length = x_right - x_left + 1
            if x_left + line_length <= test_board.columns and line_length == test_win_line:
                line_cords = {"y": y, "x_left": x_left, "x_right": x_right}
                vertical_set.append(line_cords)
            else: 
                pass
    return vertical_set

def generate_diagonally_up_set():
    du_set = []
    x_left = 1
    x_right = x_left + test_win_line - 1
    while x_right < test_board.columns:

        y_left = 1
        y_right = y_left + test_win_line - 1
        while y_right < test_board.rows:
            line_cords = {"x_left" : x_left,
                          "y_left" : y_left, 
                          "x_right" : x_right, 
                          "y_right" : y_right}
            print(line_cords)
            du_set.append(line_cords)
            y_left += 1
            y_right += 1
        x_left += 1
        x_right += 1
    return du_set
            
def choose_r_win_line(set):
    random_win_line = random.randrange(0,len(set),1)
    return set[random_win_line]

def seperate_coordinates(line):
    c_main = list(line.values())[0]
    c_higher = list(line.values())[1]
    c_lower = list(line.values())[2]
    return {"main": c_main, "higher": c_higher, "lower": c_lower}

def place_r_win_line(line_cords, set_type, sign):
    c1 = line_cords["main"]
    c_higher = line_cords["higher"]
    c_lower = line_cords["lower"]
    for c2 in range(c_higher, c_lower + 1):
        if set_type == "horizontal":
            test_board.add_checker(c1, c2, sign)
        elif set_type == "vertical":
            test_board.add_checker(c2, c1, sign)

# Uncomment code lines with type of set you want to generate a test random win line      
 
#set = generate_horizontal_set()
#set_type = "horizontal"

# set = generate_vertical_set()
# set_type = "vertical"

#set = generate_diagonally_down_set()
#set_type = "diagonally_down"

set = generate_diagonally_up_set()
set_type = "diagonally_up"
print(set)

# Choose a random line from the set and place it on the board
r_win_line = choose_r_win_line(set)
r_win_line_cords = seperate_coordinates(r_win_line)
place_r_win_line(r_win_line_cords, set_type, "X")

# Display the board with a random win line placed
test_board.refresh_board()
