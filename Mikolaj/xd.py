import tkinter as tk

class ShipPlacement:
    def __init__(self, master):
        self.master = master
        self.master.title("Umieszczanie statków - Gracz 1")
        self.board_size = 10
        self.ship_size = 4
        self.ships_to_place = 5

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Umieść swoje statki na planszy:")
        self.label.pack()

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

        self.submit_button = tk.Button(self.master, text="Zatwierdź umieszczenie statków", command=self.submit_ships)
        self.submit_button.pack()

    def toggle_ship(self, row, col):
        if self.ships_to_place > 0:
            if self.buttons[row][col].cget("bg") == "white":
                self.buttons[row][col].config(bg="black")
                self.ships_to_place -= 1
            else:
                self.buttons[row][col].config(bg="white")
                self.ships_to_place += 1

    def submit_ships(self):
        self.master.destroy()
        opponent_board = OpponentBoard()

class OpponentBoard:
    def __init__(self):
        self.opponent_board = tk.Tk()
        self.opponent_board.title("Plansza przeciwnika - Gracz 2")
        self.board_size = 10

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.opponent_board, text="Wybierz pola na planszy przeciwnika:")
        self.label.pack()

        self.board_frame = tk.Frame(self.opponent_board)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(self.board_frame, width=2, height=1,
                                   command=lambda r=row, c=col: self.make_guess(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_guess(self, row, col):
        # Tutaj można dodać logikę dla gracza 2, np. sprawdzenie trafienia i wyświetlenie rezultatu
        print(f"Gracz 2 wybrał pole: [{row}, {col}]")

def main():
    root = tk.Tk()
    placement = ShipPlacement(root)
    root.mainloop()

if __name__ == "__main__":
    main()
