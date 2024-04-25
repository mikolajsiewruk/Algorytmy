from tkinter import *
current_player=['O','X']
root = Tk()
root.title("Tic tac toe")

root.config(background="Light Green")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_height = 400
window_width = 500

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

board = [['' for _ in range(10)] for _ in range(10)]
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = Button(root,text='', font=("Arial",24),width = 6, height=3, command= lambda row = i, col = j:button_click(row,col))
        button.grid(row=i+1,column = j,padx = 5, pady= 3)
        row_buttons.append(button)
    buttons.append(row_buttons)

def button_click(row,col):
    print(current_player[-1])
    if board[row][col] == '':
        cur = current_player[-1]
        if cur =='X':
            current_player.append('O')
        else:
            current_player.append('X')
        board[row][col] = current_player[-1]
        draw_board()

def draw_board():
    for i in range(3):
        for j in range(3):
            button = buttons[i][j]
            button.config(text=board[i][j])

root.mainloop()