class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("│".join(f" {cell} " for cell in self.board[i : i + 3]))
            if i < 6:
                print("───┼───┼───")

    def update_board(self, symbol, choice):
        if self.is_valid_play(choice):
            self.board[int(choice) - 1] = symbol
            return True
        return False

    def is_valid_play(self, choice):
        return self.board[int(choice) - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


# board = Board()
# board.update_board("X", "2")
# board.display_board()
