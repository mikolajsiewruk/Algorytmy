from tkinter import *
from tkinter import messagebox
import os
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
        draw_board()
    if check_win(current_player[-1],row,col):
        messagebox.showinfo("result",f"{current_player[-1]} won")
        root.destroy()
        os.startfile("Lab8_Mikolaj.py")
    if draw_board():
        messagebox.showinfo("result", 'draw')
        root.destroy()
        os.startfile("Lab8_Mikolaj.py")

def draw_board():
    finished = True
    for i in range(10):
        for j in range(10):
            button = buttons[i][j]
            button.config(text=board[i][j])
            if buttons[i][j]['text'] == '':
                finished = False
    return finished
def check_win(player,x,y):
    win = False
    col=row=diag=rdiag=0

    for i in range(5):
        if buttons[x][i]["text"] ==player:
            col+=1
        if buttons[i][y]['text'] == player:
            row+=1
        if buttons[i][i]['text'] == player:
            diag+=1
        if buttons[i][5-i+1]['text'] == player:
            rdiag+=1
    if col == 5 or row == 5 or diag == 5 or rdiag==5:
        win = True
    print(col,row,diag,rdiag)
    return win

root.mainloop()