import tkinter as tk
from tkinter import messagebox
class Player:
    def __init__(self):
        self.ships = [[0] * 10 for _ in range(10)]
        self.available_ships = 5
    def place_ship_row(self,x,y):
        if self.available_ships == 0:
            pass
        else:
            if y+5<10:
                if self.check_row_valid_placement(x,y):
                    print(f'added in {x,y}')
                    for i in range(5):
                        self.ships[x][y+i] = 'x'
                    self.available_ships -= 1
            else:
                if self.check_col_valid_placement(x-5, y):
                    print(f'added in {x, y}')
                    for i in range(5):
                        self.ships[x][y-i] = 'x'
                    self.available_ships -= 1
        return self.ships
    def place_ship_col(self,x,y):
        if self.available_ships == 0:
            pass
        else:
            if x+5<10:
                if self.check_col_valid_placement(x,y):
                    print(f'added in {x, y}')
                    for i in range(5):
                        self.ships[x+i][y] = 'x'
                    self.available_ships -= 1
            else:
                if self.check_row_valid_placement(x,y-5):
                    print(f'added in {x, y}')
                    for i in range(5):
                        self.ships[x-i][y] = 'x'
                    self.available_ships -= 1
        return self.ships

    def cancel_ship_placement(self,x,y):
        if self.ships[x][y] == "x":
            self.ships[x][y] = 0
        else:
            messagebox.showinfo('Error',"No ship here")

        return self.ships

    def check_row_valid_placement(self,x,y):
        print(self.ships)
        for i in range(6):
            print(self.ships[x][y+i])
            if self.ships[x][y+i]=='x':
                print('xd')
                return False
        print('yea')
        return True
    def check_col_valid_placement(self,x,y):
        for i in range(6):
            print(self.ships[x+i ][y])
            if self.ships[x+i][y]=='x':
                print('xd')
                return False
        print('yes')
        return True
class ShipPlacementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ship Placement")

        self.player1 = Player()
        self.player2 = Player()
        self.current_player = self.player1
        self.board_size = 10
        self.ship_size = 5
        self.player1_ships_placed = 0
        self.player1_ships_placed = 0
        self.row = 1
        self.col = 0
        self.ship_positions = set()

        self.create_widgets()

    def create_widgets(self):
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack()

        self.reset_button = tk.Button(self.top_frame, text="Reset", command=self.reset_board)
        self.reset_button.grid(row=0, column=0)

        self.row_button = tk.Button(self.top_frame, text="Place in rows", command=self.change_placement_direction)
        self.row_button.grid(row=0, column=1)

        self.col_button = tk.Button(self.top_frame, text="Place in cols", command=self.change_placement_direction)
        self.col_button.grid(row=0, column=2)

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(self.board_frame, width=2, height=1,
                                   command=lambda r=row, c=col:self.draw_board(r,c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack()

        self.confirm_placement_button = tk.Button(self.bottom_frame, text="Confirm Placement", command=self.confirm_ship_placement)
        self.confirm_placement_button.pack()

    def reset_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(bg="SystemButtonFace")
        self.current_player.ships.clear()
        self.current_player.ships = [[0] * 10 for _ in range(10)]
        self.current_player.available_ships = 5

    def draw_board(self,row,col):
        if self.row == 1:
            self.current_player.place_ship_row(row,col)
        else:
            self.current_player.place_ship_col(row,col)


        print(self.current_player.ships)
        for i in range(len(self.current_player.ships)):
            for j in range(len(self.current_player.ships)):
                if self.current_player.ships[i][j] == 'x':
                    self.buttons[i][j].config(bg="Black")

        if self.current_player.available_ships == 0:
            messagebox.showinfo("Message","All ships placed")
    def change_placement_direction(self):
        print(self.col)
        if self.col == 1:
            self.row = 1
            self.col = 0
        else:
            self.col = 1
            self.row = 0

    def confirm_ship_placement(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            w1 = tk.Tk()
            w1.title("Player 1")

            w2 = tk.Tk()
            w2.title("Player 2")

            w1_top_frame = tk.Frame(w1)
            w1_top_frame.pack()

            w1_board_frame = tk.Frame(w1)
            w1_board_frame.pack()

            w1_buttons = []
            for row in range(self.board_size):
                button_row = []
                for col in range(self.board_size):
                    button = tk.Button(w1_board_frame, width=2, height=1,
                                       command=lambda r=row, c=col: self.draw_board(r, c))
                    button.grid(row=row, column=col)
                    button_row.append(button)
                w1_buttons.append(button_row)

            w2_top_frame = tk.Frame(w2)
            w2_top_frame.pack()

            w2_board_frame = tk.Frame(w2)
            w2_board_frame.pack()

            w2_buttons = []
            for row in range(self.board_size):
                button_row = []
                for col in range(self.board_size):
                    button = tk.Button(w2_board_frame, width=2, height=1,
                                       command=lambda r=row, c=col: self.draw_board(r, c))
                    button.grid(row=row, column=col)
                    button_row.append(button)
                w2_buttons.append(button_row)


        self.reset_board()


def main():
    root = tk.Tk()
    app = ShipPlacementGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()