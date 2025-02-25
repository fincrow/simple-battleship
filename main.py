from board import Board, BOARD_SIZE
from computer_brain import ComputerBrain
from tkinter import *
from tkmacosx import Button

computer = ComputerBrain()
my_board = Board()
com_board = Board()
show_com_board = [["" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

window = Tk()
window.title("Battleship")
window.config(padx=100, pady=50)


def make_a_guess(event):
    widget = event.widget
    position = widget.grid_info()
    x = position['column']
    y = position['row'] - 1

    try:
        if com_board.board[y][x] == "/":
            print("You've already guessed that!")
        elif com_board.board[y][x] == "O":
            print("Hit")
            com_board.hit(x, y)
            show_com_board[y][x] = "X"
            board_window.computer_buttons[y][x].config(bg="indian red")
        else:
            print("Miss")
            com_board.miss(x, y)
            show_com_board[y][x] = "/"
            board_window.computer_buttons[y][x].config(bg="powder blue")

    except IndexError:
        print("Invalid Guess! Try again")

    global player_turn
    player_turn = False


class BoardWindow:
    def __init__(self, player_board, computer_board):
        self.player_buttons = {}
        self.computer_buttons = {}
        self.generate_board(player_board, computer_board)

    def generate_board(self, player_board, computer_board):
        row_num = 0

        computer_label = Label(window, text="Computer Board")
        computer_label.grid(row=row_num, columnspan=len(player_board[0]))
        row_num += 1

        for row in computer_board:
            col_num = 0
            col_dict = {}
            for column in row:
                button = Button(window, text="", font=("Arial", 12, "bold"), highlightthickness=0, width=40)
                button.bind('<Button-1>', make_a_guess)
                button.grid(column=col_num, row=row_num)
                col_dict[col_num] = button
                col_num += 1

            self.computer_buttons[row_num-1] = col_dict
            row_num += 1

        player_label = Label(window, text="Your Board")
        player_label.grid(row=row_num, columnspan=len(player_board[0]))
        row_num += 1
        deduction = row_num

        for row in player_board:
            col_num = 0
            col_dict = {}
            for column in row:
                button = Button(window, text="", font=("Arial", 12, "bold"), highlightthickness=0, width=40)
                if column == "O":
                    button.config(bg="PaleGreen1")

                button.grid(column=col_num, row=row_num)
                col_dict[col_num] = button
                col_num += 1

            self.player_buttons[row_num-deduction] = col_dict
            row_num += 1


board_window = BoardWindow(my_board.board, com_board.board)

player_turn = True

while not com_board.completed:
    window.update()
    if my_board.completed or com_board.completed:
        for widget in window.winfo_children():
            widget.destroy()
        break
    while not player_turn:
        computer.random_guess(my_board, board_window.player_buttons)
        player_turn = True

window.mainloop()
