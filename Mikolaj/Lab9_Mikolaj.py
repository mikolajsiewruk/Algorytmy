import tkinter as tk
from tkinter import messagebox
class Player:
    def __init__(self):
        self.ships = [[0] * 10 for _ in range(10)]
        self.available_ships = 5
    def place_ship_row(self,x,y):
        if y+5<10:
            for i in range(5):
                self.ships[x][y+i] = 'x'
        else:
            for i in range(5):
                self.ships[x][y-i] = 'x'
        return self.ships
    def place_ship_col(self,x,y):
        if x+5<10:
            for i in range(5):
                self.ships[x+i][y] = 'x'
        else:
            for i in range(5):
                self.ships[x-i][y] = 'x'
        return self.ships

    def cancel_ship_placement(self,x,y):
        if self.ships[x][y] == "x":
            self.ships[x][y] = 0
        else:
            messagebox.showinfo('Error',"No ship here")

        return self.ships
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

        self.confirm_button = tk.Button(self.top_frame, text="Confirm Placement", command=self.confirm_placement)
        self.confirm_button.grid(row=0, column=1)

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(self.board_frame, width=2, height=1,
                                   command=lambda r=row, c=col: self.toggle_ship(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack()

        self.confirm_placement_button = tk.Button(self.bottom_frame, text="Confirm Placement", command=self.confirm_placement)
        self.confirm_placement_button.pack()

    def reset_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(bg="SystemButtonFace")
        self.ship_positions.clear()
        self.ships_placed = 0

    def toggle_ship(self, row, col):
        if self.row == 1:
            self.current_player.place_ship_row(row,col)
            if col+5<=10:
                for i in range(5):
                    self.buttons[row][col+i].config(bg="Black")
            else:
                for i in range(5):
                    self.buttons[row][col-i].config(bg="Black")
        else:
            self.current_player.place_ship_col(row,col)

    def confirm_placement(self):
        if self.ships_placed == self.ship_size:
            print("Placement confirmed:", self.ship_positions)
            # Here you can add logic to pass ship_positions to the next step of the game
        else:
            print("Please place exactly 5 ships.")

b = Player()
b.place_ship_col(1,1)


def main():
    root = tk.Tk()
    app = ShipPlacementGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()