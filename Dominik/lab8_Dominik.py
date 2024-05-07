from tkinter import *
from tkinter import messagebox


def clear_board():
    for i in range(10):
        for j in range(10):
            board[i][j] = ""
    global current_player
    current_player = "O"
    label.config(text="Current player is: " + current_player)


# Function offering players to play again
def play_again():
    res = messagebox.askyesno('Again?', 'Do you want to play again?')
    if res:
        clear_board()
        draw_board()
    else:
        window.destroy()


# Function checking for all possible win conditions
def check_win(player):
    counter = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == "O" or board[i][j] == "X":
                counter += 1
            if board[i][j:j+5] == [player, player, player, player, player]:
                messagebox.showinfo("Game Over", player + " wins")
                play_again()
            elif j < 6 and all(board[j + x][i] == player for x in range(5)):
                print(player, "wins")
                messagebox.showinfo("Game Over", player + " wins")
                play_again()
            elif j < 6 and i < 6 and all(board[j + x][i+x] == player for x in range(5)):
                messagebox.showinfo("Game Over", player + " wins")
                play_again()
            elif j < 6 and i > 5 and all(board[j + x][i-x] == player for x in range(5)):
                messagebox.showinfo("Game Over", player + " wins")
                play_again()
            elif counter == 100:
                messagebox.showinfo("Game Over", "Draw")
                play_again()


# Function editing the board by adding the symbol to pressed button
def draw_board():
    for i in range(10):
        for j in range(10):
            button = buttons[i][j]
            if board[i][j] == "O":
                button.config(text=board[i][j], fg="Blue")
            else:
                button.config(text=board[i][j], fg="Red")


# Function responding to pressing the button
def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        draw_board()
        current_player = "O" if current_player == "X" else "X"
        label.config(text="Current player is: " + current_player)
        check_win("O")
        check_win("X")


# Window configuration
window = Tk()

# Basic confs - title, transparency, icon, colour
window.title("Tic tac toe")
window.attributes("-alpha", 0.9)
window.call('wm', 'iconphoto', window._w,
            PhotoImage(file='tictactoe.png'))
window.config(background='#4e11e9')

# Window placement on screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 900
window_height = 790
center_x = center_y = int(screen_width / 2 - window_width / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Board as a list
board = [['' for _ in range(10)] for _ in range(10)]

current_player = "O"
label = Label(window, text="Current player is: " + current_player, font=("Arial", 16), bg="#4e11e9", fg="white")
label.grid(row=0, columnspan=10, pady=(5, 10))

# Creating buttons
buttons = []
for i in range(10):
    row_buttons = []
    for j in range(10):

        button = Button(window, text="", font=("Arial", 24), width=3, height=2, cursor='hand2',
                        anchor="center", command=lambda row=i, col=j: button_click(row, col))

        button.grid(row=i + 1, column=j, padx=5, pady=3)
        row_buttons.append(button)
    buttons.append(row_buttons)

window.mainloop()
