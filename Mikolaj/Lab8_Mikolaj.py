from tkinter import *
from tkinter import messagebox
import os
current_player=['O','X']
root = Tk()
root.title("Tic tac toe")

root.config(background="Blue")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_height = 690
window_width = 770

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

board = [['' for _ in range(10)] for _ in range(10)]
buttons = []
for i in range(10):
    row_buttons = []
    for j in range(10):
        button = Button(root,text='', font=("Arial",24),width = 3, height=1, command= lambda row = i, col = j:button_click(row,col))
        button.grid(row=i+1,column = j,padx = 5, pady= 3)
        row_buttons.append(button)
    buttons.append(row_buttons)

def button_click(row,col):
    if board[row][col] == '':
        cur = current_player[-1]
        if cur =='X':
            current_player.clear()
            current_player.append('O')
        else:
            current_player.clear()
            current_player.append('X')
        board[row][col] = current_player[-1]
        print(board)
        draw_board()
    if check_win(current_player[-1],row,col):
        messagebox.showinfo("result",f"{current_player[-1]} won")
        clear_board()
        draw_board()
    if draw_board():
        clear_board()
        draw_board()

def draw_board():
    finished = True
    for i in range(10):
        for j in range(10):
            button = buttons[i][j]
            button.config(text=board[i][j])
            if buttons[i][j]['text'] == '':
                finished = False
    return finished

def clear_board():
    for i in range(10):
        for j in range(10):
            board[i][j] = ""
    current_player.append("O")
def check_win(player,x,y):
    win = False
    col=row=diag=rdiag=1
    col_b=row_b=diag_b=rgiag_b=0
    print(player)
    print(x,y)
    k=1
    while x+k <10 and y+k <10:
        while buttons[x+k][y+k]['text'] == player:
            diag += 1
            k+=1
        break
    while x-k>-1 and y-k>-1:
        while buttons[x-k][y-k]['text'] == player:
            diag+=1
            k+=1
        break
    while x+k<10 and y-k>-1:
        while buttons[x+k][y-k]['text'] == player:
            rdiag+=1
            k+=1
        break
    while x-k>-1 and y+k<10:
        while buttons[x-k][y+k]['text'] == player:
            rdiag+=1
            k+=1
        break
    while y+k <10:
        while buttons[x][y+k]["text"] ==player:
            k+=1
            row+=1
        break
    while y-k>-1:
        while buttons[x][y-k]["text"] ==player:
            row+=1
            k+=1
        break
    while x+k<10:
        while buttons[x+k][y]['text'] == player:
            col+=1
            k+=1
        break
    while x-k>-1:
        while buttons[x - k][y]['text'] == player:
            col+=1
            k+=1
        break
    if col == 5 or row == 5 or diag == 5 or rdiag==5:
        win = True
    return win

root.mainloop()