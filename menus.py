TOP_LEFT = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
HORIZONTAL = "═"
VERTICAL = "║"

class Menus:
    def display_main_menu(self):
        while True:
            Menus.print_message_dynamically_with_border(
                self, "Welcome to Tic Tac Toe game"
            )
            print("  1. Start Game")
            print("  2. Quit Game")
            choice = input("Enter choice (1 or 2): ")
            if choice in ("1", "2"):
                return choice
            print("Error: Invalid choice please try again\n")

    def display_end_game_menu(self):
        while True:
            Menus.print_message_dynamically_with_border(self, "Game Over! Player1 wins")
            print("  1. Restart Game")
            print("  2. Quit Game")
            choice = input("Enter choice (1 or 2): ")
            if choice in ("1", "2"):
                return choice
            print("Error: Invalid choice please try again\n")

    def print_message_dynamically_with_border(self, message):
        width = len(message) + 4  # 4 extra spaces
        Menus.print_horizontal_border(self, "TOP", width)
        Menus.print_message_row(self, message)
        Menus.print_horizontal_border(self, "BOTTOM", width)

    def print_horizontal_border(self, vertical_location, width):
        left_var = f"{vertical_location}_LEFT"
        right_var = f"{vertical_location}_RIGHT"

        print(globals()[left_var], end="")
        print("".join(globals()["HORIZONTAL"] for _ in range(width)), end="")
        print(globals()[right_var])

    def print_message_row(self, message):
        print(f"{globals()['VERTICAL']}  {message}  {globals()['VERTICAL']}")


# menus = Menus()
# menus.display_main_menu()
# menus.display_end_game_menu()
