import turn_control as turn_c
import board_control as board_c
import player_control as player_c
import datetime

class Game:
    game_counter = 0
    def __init__(self):
        # Unique identification and information about the game
        Game.game_counter += 1
        self.id = Game.game_counter
        self.date = datetime.date.today().strftime('%d-%m-%Y')
        self.turn_count = 0
        self.winner = "Tie"
        # Assign a new board for the game and save final board status
        self.board = board_c.Board()
        self.board_final = None
        # Assign players for the game
        self.players_amount = 2
        self.players = [None for i in range(self.players_amount)]
    
    # Define players and create Player instances
    def add_players(self):
        for index in range(len(self.players)):
            new_player = player_c.Player()
            new_player.set_name()
            new_player.set_checker_sign(self.board)
            # Add new Player instance to the list of players assigned to this game
            self.players[index] = new_player
    
    # Choose starting player by comparing random order attributes of each player
    def set_player_order(self):
        player1 = self.players[0]
        player2 = self.players[1]
        if player1.order < player2.order:
            temp_player = player1
            self.players[0] = player2
            self.players[1] = temp_player

# Start a new game
game = Game()
# Set up players and order
game.add_players()
game.set_player_order()
print(game.players)

# Set up board and display it
game.board.generate_board()
game.board.refresh_board()

# Loop untill the win conditions are met
win_conditions = False
while(win_conditions == False):
    # Choose and save current player
    # Choice is determined by the remainder of dividing the current turn by total amount of players
    # EXAMPLE: Current turn = 5, Players amount = 2, 5 / 2 = 2*2 + 1 <--
    # EXAMPLE: Remainder from this operation is 1, so the player under index 1 (so Player 2) is the turn owner
    current_player = game.players[game.turn_count % game.players_amount]
    # Prepare new turn and start it
    current_turn = turn_c.Turn(current_player, game.turn_count)
    current_turn.start_turn()
    # Prepare new checker and place it
    current_checker = current_turn.place_checker(game.board)
    # Add the checker to the board and refresh it so it displays new board status
    game.board.add_checker(current_checker.x_pos, current_checker.y_pos, current_player.checker_sign)
    game.board.refresh_board()
    # Increment total turn counter by 1
    game.turn_count += 1
    # Check if winning conditions were met, if yes then end the game
    win_conditions = current_turn.check_vertical_status(game.board)
