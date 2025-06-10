class Player:
    names = []
    symbols = []

    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name: (Letters only) ")
            if name.isalpha():
                name = name.title()
                if name not in Player.names:
                    self.name = name
                    Player.names.append(name)
                    break
                else:
                    print("Error: Name already taken. Choose another one.")

            else:
                print("Error: Invalid name please enter name with letters only")

    def choose_symbol(self):
        while True:
            symbol = input("Enter your Symbol: (One Character) ")
            if symbol.isalpha() and len(symbol) == 1:
                symbol = symbol.upper()

                if symbol not in Player.symbols:
                    self.symbol = symbol
                    Player.symbols.append(symbol)
                    break
                else:
                    print("Error: Symbol already taken. Choose another one.")

            else:
                print("Error: Invalid symbol please enter one character as a symbol")
