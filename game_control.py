import turn_control as turn_c
import board_control as board_c
import player_control as player_c

board1 = board_c.Board()
board1.generate_board()

turn1 = turn_c.Turn(player1, board1)
turn1.start_turn()

checker = turn1.place_checker()
board1.add_checker(checker.x_pos, checker.y_pos, player1.checker_sign)
print(board1.board_array)
board1.refresh_board()

