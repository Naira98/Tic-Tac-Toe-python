TOP_LEFT = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
HORIZONTAL = "═"
VERTICAL = "║"

class Utils():
    def print_message_dynamically_with_border(self, message):
        width = len(message) + 4  # 4 extra spaces
        self.print_horizontal_border("TOP", width)
        self.print_message_row( message)
        self.print_horizontal_border("BOTTOM", width)

    @staticmethod
    def print_horizontal_border(vertical_location, width):
        left_var = f"{vertical_location}_LEFT"
        right_var = f"{vertical_location}_RIGHT"

        print(globals()[left_var], end="")
        print("".join(globals()["HORIZONTAL"] for _ in range(width)), end="")
        print(globals()[right_var])

    @staticmethod
    def print_message_row(message):
        print(f"{globals()['VERTICAL']}  {message}  {globals()['VERTICAL']}")