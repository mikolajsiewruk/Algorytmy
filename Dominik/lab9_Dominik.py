from tkinter import *
from tkinter import messagebox
from tkmacosx import Button


# Putting pieces on the board at the beginning fo the game
def starting_position():
    for i in range(8):
        for j in range(8):
            button = buttons[i][j]
            if i in [0, 1] and button.cget('bg') == 'black':  # Placing red pawns
                button.config(text="O", fg="Red")
                board[i][j] = "O"
            elif i in [6, 7] and button.cget('bg') == 'black':  # Placing blue pawns
                button.config(text="O", fg="Blue")
                board[i][j] = "O"


# Redrawing the board after every update
def draw_board(row, col):
    for i in range(8):
        for j in range(8):
            button = buttons[i][j]
            # Drawing the "just moved" pawn figure; can't do regular if because the i j square has no colour: pawn disappears
            if i == row and j == col:
                button.config(text=board[i][j], fg=current_player)
            # Drawing the "not moved" figures in the right colour
            elif board[i][j] == "O" or board[i][j] == "Q":
                button.config(text=board[i][j], fg=button.cget('fg'))
            # Drawing empty squares
            else:
                button.config(text=board[i][j])


# Set of functions checking if there's a possible take for a pawn of current_player
def left_down(row, col):
    if row<6 and col>1 and board[row][col] == "O":
        button = buttons[row+1][col-1]
        if board[row+1][col-1] != "" and button.cget("fg") != current_player and board[row+2][col-2] == "":
            return True
    return False


def left_up(row, col):
    if row>1 and col>1 and board[row][col] == "O":
        button = buttons[row-1][col-1]
        if board[row-1][col-1] != "" and button.cget("fg") != current_player and board[row-2][col-2] == "":
            return True
    return False


def right_up(row, col):
    if row>1 and col<6 and board[row][col] == "O":
        button = buttons[row-1][col+1]
        if board[row-1][col+1] != "" and button.cget("fg") != current_player and board[row-2][col+2] == "":
            return True
    return False


def right_down(row, col):
    if row<6 and col<6 and board[row][col] == "O":
        button = buttons[row+1][col+1]
        if board[row+1][col+1] != "" and button.cget("fg") != current_player and board[row+2][col+2] == "":
            return True
    return False


def force_take(row, col):
    button = buttons[row][col]
    if board[row][col] != "" and button.cget("fg") == current_player:
        if right_up(row, col) or right_down(row, col) or left_down(row, col) or left_up(row, col):
            return True
    return False


# Checking if a move is correct (regular move, take) for pawn and queen
# Then performing the move with all its consequences
def is_correct(row, col):
    if board[old_row][old_col] == "O":  # Correctness for pawns
        if current_player == "Red":  # Correctness for red pawns
            if row == old_row + 1 and (col == old_col + 1 or col == old_col - 1):  # Moving forward
                board[old_row][old_col] = ""
                if row == 7:  # Checking for promotion to queen
                    board[row][col] = "Q"
                else:
                    board[row][col] = "O"
                draw_board(row, col)
                return True
            # Taking in all four directions
            elif (row == old_row + 2 or row == old_row - 2) and (col == old_col + 2 or col == old_col - 2):
                mean_row = int((row + old_row) / 2)
                mean_col = int((col + old_col) / 2)
                pawn = buttons[mean_row][mean_col]
                pawn_colour = pawn.cget("fg")
                # Checking if the figure is opposite colour
                if board[mean_row][mean_col] != "" and pawn_colour == "Blue":
                    board[mean_row][mean_col] = ""  # Actually taking
                    board[old_row][old_col] = ""
                    if row == 7:  # Checking for promotion to queen
                        board[row][col] = "Q"
                    else:
                        board[row][col] = "O"
                    draw_board(row, col)
                    return True
            else:
                return False

        elif current_player == "Blue":  # Correctness for blue pawns
            if row == old_row - 1 and (col == old_col + 1 or col == old_col - 1):  # Moving forward
                board[old_row][old_col] = ""
                if row == 0:  # Checking for promotion to queen
                    board[row][col] = "Q"
                else:
                    board[row][col] = "O"
                draw_board(row, col)
                return True
            # Taking in all four directions
            elif (row == old_row + 2 or row == old_row - 2) and (col == old_col + 2 or col == old_col - 2):
                mean_row = int((row + old_row) / 2)
                mean_col = int((col + old_col) / 2)
                pawn = buttons[mean_row][mean_col]
                pawn_colour = pawn.cget("fg")
                # Checking if the figure is opposite colour
                if board[mean_row][mean_col] != "" and pawn_colour == "Red":
                    board[mean_row][mean_col] = ""  # Actually taking
                    board[old_row][old_col] = ""
                    if row == 0:  # Checking for promotion to queen
                        board[row][col] = "Q"
                    else:
                        board[row][col] = "O"
                    draw_board(row, col)
                    return True
            else:
                return False

    else:  # Correctness for queens
        pieces = 0  # Counter of opponent's pawn in straight diagonal
        if old_row < row:  # Moving down
            if old_col < col:  # Moving right
                for i, j in zip(range(old_row+1, row), range(old_col+1, col)):
                    if board[i][j] != "":  # Detecting figures in the way
                        pawn = buttons[i][j]
                        pawn_colour = pawn.cget("fg")
                        if pawn_colour == current_player:  # Can't take your own figure
                            return False
                        else:
                            pieces += 1  # Figures in line counter
                if pieces < 2:  # If a take is legal
                    board[old_row][old_col] = ""
                    board[row][col] = "Q"
                    for i, j in zip(range(old_row+1, row), range(old_col+1, col)):
                        board[i][j] = ""
                        draw_board(row, col)
                    return True
                else:
                    return False
            else:
                for i, j in zip(range(old_row+1, row), range(old_col-1, col, -1)):
                    if board[i][j] == "O" or board[i][j] == "Q":
                        pawn = buttons[i][j]
                        pawn_colour = pawn.cget("fg")
                        if pawn_colour == current_player:
                            return False
                        else:
                            pieces += 1
                if pieces < 2:
                    board[old_row][old_col] = ""
                    board[row][col] = "Q"
                    for i, j in zip(range(old_row+1, row), range(old_col-1, col, -1)):
                        board[i][j] = ""
                        draw_board(row, col)
                    return True
                else:
                    return False
        else:
            if old_col - col < 0:
                for i, j in zip(range(old_row-1, row, -1), range(old_col+1, col)):
                    if board[i][j] == "O" or board[i][j] == "Q":
                        pawn = buttons[i][j]
                        pawn_colour = pawn.cget("fg")
                        if pawn_colour == current_player:
                            return False
                        else:
                            pieces += 1
                if pieces < 2:
                    board[old_row][old_col] = ""
                    board[row][col] = "Q"
                    for i, j in zip(range(old_row-1, row, -1), range(old_col+1, col)):
                        board[i][j] = ""
                        draw_board(row, col)
                    return True
                else:
                    return False
            else:
                for i, j in zip(range(old_row-1, row, -1), range(old_col-1, col, -1)):
                    if board[i][j] == "O" or board[i][j] == "Q":
                        pawn = buttons[i][j]
                        pawn_colour = pawn.cget("fg")
                        if pawn_colour == current_player:
                            return False
                        else:
                            pieces += 1
                if pieces < 2:
                    board[old_row][old_col] = ""
                    board[row][col] = "Q"
                    for i, j in zip(range(old_row-1, row, -1), range(old_col-1, col, -1)):
                        board[i][j] = ""
                        draw_board(row, col)
                    return True
                else:
                    return False


# Checking if someone won
def win_condition():
    red_counter, blue_counter = 0, 0
    for i in range(8):
        for j in range(8):
            button = buttons[i][j]
            if board[i][j] == "O" and button.cget('fg') == "Blue":
                blue_counter =+ 1
            elif board[i][j] == "O" and button.cget('fg') == "Red":
                red_counter =+ 1
    if blue_counter == 0:
        messagebox.showinfo("Game over",  "Red wins")
        window.destroy()
    elif red_counter == 0:
        messagebox.showinfo("Game Over", "Blue wins")
        window.destroy()


# What happens at each button click
# Also passing the turn to the next player
def button_click(row, col):
    global current_player
    global old_row
    global old_col
    global colour
    global must
    button = buttons[row][col]
    for i in range(8):
        for j in range(8):
            if force_take(i, j):
                must = 1

    if must == 1:
        if board[row][col] != "" and button.cget("fg") == current_player:
            if force_take(row, col):
                colour = button.cget("fg")
                old_row = row
                old_col = col

        elif board[row][col] == "" and old_row != -1 and abs(row-old_row) > 1 and is_correct(row, col):
            old_row = -1
            old_col = -1
            colour = None
            must = 0
            if force_take(row, col):
                current_player = current_player
            else:
                current_player = "Blue" if current_player == "Red" else "Red"
                label.config(text="Current player is: " + current_player)
                win_condition()
    else:
        if board[row][col] !="" and button.cget("fg") == current_player:
            colour = button.cget("fg")
            old_row = row
            old_col = col

        elif board[row][col] == "" and old_row != -1 and is_correct(row, col):
            old_row = -1
            old_col = -1
            colour = None
            current_player = "Blue" if current_player == "Red" else "Red"
            label.config(text="Current player is: " + current_player)
            win_condition()



window = Tk()

# Window configuration
window.title("Checkers")
window.config(background="maroon")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 900
window_height = 790
center_x = center_y = int(screen_width / 2 - window_width / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Board creation
board = [['' for _ in range(8)] for _ in range(8)]

# Global variables starting values
old_row = -1
old_col = -1
must = 0
colour = None
current_player = "Blue"

# Current player label
label = Label(window, text="Current player is: " + current_player, font=("Arial", 14), bg = 'maroon', fg="white")
label.grid(row=0, columnspan=10, pady=(0, 0))

# Creating buttons
buttons = []
for i in range(8):
    row_buttons = []
    for j in range(8):
        if (i%2 == 1 and j%2 == 0) or (i%2 == 0 and j%2 == 1):
            button = Button(window, text="", font=("Arial", 72), width=100, height=90, cursor='hand2', bg="black",
                            borderless=1, anchor="center", command=lambda row=i, col=j: button_click(row, col))
        else:
            button = Button(window, text="", font=("Arial", 72), width=100, height=90, cursor='hand2', bg="white",
                            borderless=1, anchor="center", command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i + 1, column=j, padx=5, pady=3)
        row_buttons.append(button)
    buttons.append(row_buttons)

starting_position()

window.mainloop()