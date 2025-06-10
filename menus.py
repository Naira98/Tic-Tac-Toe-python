from utils import Utils

class Menus:
    def display_main_menu(self):
        while True:
            Utils().print_message_dynamically_with_border("Welcome to Tic Tac Toe game")
            print("  1. Start Game")
            print("  2. Quit Game")
            choice = input("Enter choice (1 or 2): ")
            if choice in ("1", "2"):
                return int(choice)
            print("Error: Invalid choice please try again\n")

    def display_end_game_menu(self, message):
        while True:
            Utils().print_message_dynamically_with_border(message)
            print("  1. Restart Game")
            print("  2. Quit Game")
            choice = input("Enter choice (1 or 2): ")
            if choice in ("1", "2"):
                return int(choice)
            print("Error: Invalid choice please try again\n")
