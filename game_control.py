import turn_control as turn_c
import board_control as board_c
import player_control as player_c
import datetime

class Game:
    game_counter = 0
    def __init__(self):
        Game.game_counter += 1
        self.id = Game.game_counter
        self.players_amount = 2
        self.board = board_c.Board()
        self.date = datetime.date.today().strftime('%d-%m-%Y')
        self.turn_count = 0
        self.board_final = None
        print(self.date)
    
    def add_players(self):
        players_count = 0
        players = []
        while(players_count < self.players_amount):
            new_player = player_c.Player()
            new_player.set_name()
            new_player.set_checker_sign(self.board)
            players.append(new_player)
            players_count += 1
        return players
    

    def set_player_order(self, players):
        player1 = players[0]
        player2 = players[1]
        if player1.order < player2.order:
            temp_player = player1
            player1 = player2
            player2 = temp_player
        return player1, player2



new_game = Game()
players = new_game.add_players()
player1, player2 = new_game.set_player_order(players)
print(player1.name, player2.name)



board1 = board_c.Board()
board1.generate_board()

turn1 = turn_c.Turn(player1, board1)
turn1.start_turn()

checker = turn1.place_checker()
board1.add_checker(checker.x_pos, checker.y_pos, player1.checker_sign)
print(board1.board_array)
board1.refresh_board()

