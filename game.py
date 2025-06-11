from board import Board
from player import Player
from menus import Menus
from utils import Utils


class Game:
    def __init__(self):
        self.board = Board()
        self.menus = Menus()
        self.players = [Player(), Player()]
        self.current_player_index = 0

    def start_game(self):
        choice = self.menus.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for idx, player in enumerate(self.players, 1):
            Utils().print_message_dynamically_with_border(f"Player {idx}")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            message = ""
            if self.is_win():
                message = f"Congratulations {self.players[self.current_player_index].name} wins!"
            elif self.is_draw():
                message = "Game Over. It's a draw!"
                self.current_player_index = 0
                pass
            if message:
                choice = self.menus.display_end_game_menu(message)
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                break
            self.switch_player()

    def play_turn(self):
        Utils().clear_terminal()
        player = self.players[self.current_player_index]

        while True:
            self.board.display_board()

            print(f"\n{player.name}'s turn ({player.symbol})")
            try:
                choice = int(input("Choose a cell (1-9): "))
                if 1 <= choice <= 9 and self.board.update_board(player.symbol, choice):
                    Utils().clear_terminal()
                    self.board.display_board()
                    break
                else:
                    print("Error: Invalid move, try again.\n")
            except ValueError:
                print("Error: Please enter number between 1 and 9.\n")

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def is_win(self):
        win_probabilities = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]

        for probability in win_probabilities:
            if (
                self.board.board[probability[0]]
                == self.board.board[probability[1]]
                == self.board.board[probability[2]]
            ):
                return True
        return False

    def is_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.play_game()

    def quit_game(self):
        print("Thank you for playing. Goodbye!")

