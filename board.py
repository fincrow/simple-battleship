import random

BOARD_SIZE = 6
ships = {
    # "ship_1": ["O", "O", "O", "O", "O"],
    "ship_2": ["O", "O", "O", "O"],
    "ship_3": ["O", "O", "O"],
    "ship_4": ["O", "O"]
}


class Board:
    def __init__(self):
        self.board = [["" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        self.setup_board(ships)
        self.completed = False

    def setup_board(self, ships: dict):
        for name, ship in ships.items():
            horizontal_or_vertical = random.choice(["horizontal", "vertical"])

            if horizontal_or_vertical == "horizontal":
                coords = self.generate_coordinates(ship, horizontal_or_vertical)
                x = coords[0]
                y = coords[1]

                ship_placed = False
                while not ship_placed:
                    if not self.check_if_ship(self.board, x, y, ship, horizontal_or_vertical):
                        self.place_ship(self.board, x, y, ship, horizontal_or_vertical)
                        ship_placed = True
                    else:
                        coords = self.generate_coordinates(ship, horizontal_or_vertical)
                        x = coords[0]
                        y = coords[1]

            if horizontal_or_vertical == "vertical":
                coords = self.generate_coordinates(ship, horizontal_or_vertical)
                x = coords[0]
                y = coords[1]

                ship_placed = False
                while not ship_placed:
                    if not self.check_if_ship(self.board, x, y, ship, horizontal_or_vertical):
                        self.place_ship(self.board, x, y, ship, horizontal_or_vertical)
                        ship_placed = True
                    else:
                        coords = self.generate_coordinates(ship, horizontal_or_vertical)
                        x = coords[0]
                        y = coords[1]

    def generate_coordinates(self, func_ship, horizontal_vertical):
        if horizontal_vertical == "horizontal":
            rand_y = random.randint(0, len(self.board) - 1)
            rand_x = random.randint(0, (len(self.board[rand_y]) - len(func_ship)))
        else:
            rand_x = random.randint(0, len(self.board) - 1)
            rand_y = random.randint(0, (len(self.board[rand_x]) - len(func_ship)))

        return rand_x, rand_y

    def check_if_ship(self, board, x_co, y_co, func_ship, horizontal_vertical):
        if horizontal_vertical == "horizontal":
            for space in range(len(func_ship)):
                if board[y_co][x_co + space] == "O":
                    print("Something's here")
                    return True
        else:
            for space in range(len(func_ship)):
                if board[y_co + space][x_co] == "O":
                    print("Something's here")
                    return True

    def place_ship(self, board, x_co, y_co, func_ship, horizontal_vertical):
        if horizontal_vertical == "horizontal":
            for space in range(len(func_ship)):
                board[y_co][x_co + space] = func_ship[space]
        else:
            for space in range(len(func_ship)):
                board[y_co + space][x_co] = func_ship[space]

    def hit(self, x, y):
        self.board[y][x] = "X"
        remaining_boat = any("O" in sublist for sublist in self.board)

        if not remaining_boat:
            self.completed = True
            print("Game Over")
            return self.completed

    def miss(self, x, y):
        self.board[y][x] = "/"
