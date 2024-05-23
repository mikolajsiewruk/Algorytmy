import tkinter as tk
from tkinter import messagebox

class Owca:
    def __init__(self, row, col, index):
        self.row = row
        self.col = col
        self.index = index

    def get_position(self):
        return self.row, self.col #zwraca aktualną pozycję owcy


    def set_position(self, row, col):
        self.row = row
        self.col = col

class Wilk:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col

class Gracz:
    def __init__(self, name, role=None):
        self.name = name # ('sheep' - owca, 'wolf' - wilk)

        self.role = role

class Gra:
    def __init__(self, gracz1, gracz2, tlo):
        self.gracz1 = gracz1
        self.gracz2 = gracz2
        self.aktualny_gracz = self.gracz1
        self.canvas = tlo
        self.wilk = Wilk(0, 0)
        self.owca = [Owca(7, i, idx) for idx, i in enumerate(range(1, 8, 2))] #owce w odpowiednich pozycjach
        self.draw_board()

    def draw_board(self):
        for i in range(9): #rysowanie linii planszy
            self.canvas.create_line(0, i * 50, 400, i * 50)
            self.canvas.create_line(i * 50, 0, i * 50, 400)

        for sheep in self.owca:
            row, col = sheep.get_position()
            self.canvas.create_oval(col * 50 + 10, row * 50 + 10, col * 50 + 40, row * 50 + 40, fill='white') #owieczki jako białe

        row, col = self.wilk.get_position()
        self.canvas.create_rectangle(col * 50 + 10, row * 50 + 10, col * 50 + 40, row * 50 + 40, fill='gray') #wilk szary

    def switch_player(self):
        self.aktualny_gracz = self.gracz2 if self.aktualny_gracz == self.gracz1 else self.gracz1

    def move_wilk(self, row, col):
        if self.aktualny_gracz.role == 'wilk':
            if self.is_valid_move(self.wilk.get_position(), (row, col)):
                self.wilk.set_position(row, col)
                self.switch_player()
                self.draw_board()
                self.check_game_over()

    def move_owca(self, sheep_index, row, col):
        if self.aktualny_gracz.role == 'owca':
            sheep = self.owca[sheep_index]
            if self.is_valid_move(sheep.get_position(), (row, col)):
                sheep.set_position(row, col)
                self.switch_player()
                self.draw_board()
                self.check_game_over()

    def is_valid_move(self, from_pos, to_pos):
        from_row, from_col = from_pos #aktualna pozycja
        to_row, to_col = to_pos #nowa pozycja
        if to_row < 0 or to_row > 7 or to_col < 0 or to_col > 7: #sprawdzenie czy jest w granicach planszy
            return False
        if (to_row, to_col) == self.wilk.get_position() or (to_row, to_col) in [sheep.get_position() for sheep in self.owca]: #sprawdzenie czy nie stoi tam juz jakis pionek
            return False
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if self.aktualny_gracz.role == 'wilk':
            return row_diff == 1 and col_diff == 1 #wilk może ruszać się tylko o jedno pole na ukos do przodu i tyłu
        else:
            return row_diff == 1 and col_diff == 1 and to_row > from_row #owca może ruszać się tylko do przodu o jedno pole na ukos
    def check_game_over(self):
        if self.wilk_jest_zwyciezca():
            messagebox.showinfo("Koniec gry", "Wilk wygrywa")
            self.canvas.quit()
        elif self.owca_jest_zwyciezca():
            messagebox.showinfo("Koniec gry", "Owce wygrywają")
            self.canvas.quit()
        elif self.is_blocked():
            messagebox.showinfo("Koniec gry", "Owce zablokowały wilka")
            self.canvas.quit()

    def wilk_jest_zwyciezca(self):
        return self.wilk.get_position()[1] == 7 #sprawdzenie czy wilk dotarł do owiec

    def owca_jest_zwyciezca(self):
        return all(owca.get_position()[1] == 0 for owca in self.owca)

    def is_blocked(self):
        row, col = self.wilk.get_position()
        moves = [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
        return all(move in [owca.get_position() for owca in self.owca] for move in moves) #sprawdzenie czy owce zablokowały wilka

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wilk i owce")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        gracz1 = Gracz("Gracz 1", role='owce')
        gracz2 = Gracz("Gracz 2", role='wilk')
        self.game = Gra(gracz1, gracz2, self.canvas)

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        col = event.x // 50
        row = event.y // 50

        if self.game.aktualny_gracz.role == 'wilk':
            self.game.move_wilk(row, col)
        elif self.game.aktualny_gracz.role == 'owce':
            for i, sheep in enumerate(self.game.owca):
                if sheep.get_position() == (row, col):
                    self.game.move_owca(i, row, col)
                    break

if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
