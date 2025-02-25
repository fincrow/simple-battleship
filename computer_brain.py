import random
from board import BOARD_SIZE

class ComputerBrain:
    def __init__(self):
        self.last_guess = None

    def random_guess(self, inp_board, buttons):
        # Generate random coordinates
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)

        # Check if the position has already been guessed
        while inp_board.board[y][x] in ["/", "X"]:
            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)

        # Process the guess
        if inp_board.board[y][x] == "O":
            self.last_guess = True
            inp_board.hit(x=x, y=y)
            buttons[y][x].config(bg="indian red")
        else:
            self.last_guess = False
            inp_board.miss(x=x, y=y)
            buttons[y][x].config(bg="powder blue")