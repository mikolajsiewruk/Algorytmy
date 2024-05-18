class Sheep:
    def __init__(self, row, col, index):
        self.row = row
        self.col = col
        self.index = index
        self.position = (row, col) #pozycja owcy

    def get_position(self):
        return self.position

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_index(self):
        return f"sheep{self.index}"

class Wolf:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_position(self): #aktualna pozycja owcy
        return self.row, self.col

    def set_position(self, row, col): #nowa pozycja owcy
        self.row = row
        self.col = col


class Game:
    def __init__(self, player, player2, session):
        self.player1 = player
        self.player2 = player2
        self.session = session
        self.players = [self.player, self.player2]
        self.current_player = self.player
        self.last_move = None
        self.player_role = None
        self.user_move_completed = False
        self.move_history = {"owca": [], "wilk": []}
        self.wolf = Wolf(0, 0)
        self.sheep = [Sheep(2 * i, 7, j) for i in range(1, 8, 2) for j in range(4)] #owce w odpowiednich pozycjach

    def get_wolf(self):
        return self.wolf

    def get_sheep(self):
        return self.sheep

    def set_player_role(self, role):
        if role == 'owca':
            self.player1.set_player_role(role)
            self.player2.set_player_role('wilk')
        elif role == 'wilk':
            self.player1.set_player_role(role)
            self.player2.set_player_role('owca')
        else:
            raise ValueError(f"Nieznana rola: {role}")

    def switch_player(self):
        self.current_player = (
            self.player if self.current_player == self.player2 else self.player2
        )

    def is_player_turn(self):
        print(f"DEBUG: Checking if it's player's turn. Current player: {self.current_player.get_role()}")
        return self.current_player == self.player

    def get_move_history(self):
        print(f"Komputer widzi grę jako {self.current_player.get_role()}")
        player_role = self.current_player.get_player_role() if self.current_player.get_player_role() is not None\
            else 'owca'

    def is_game_over(self):
        if self.is_wolf_winner():
            print("Wilk wygrywa")
            return True, "Wilk wygrywa!"
        elif self.is_sheep_winner():
            print("Owca wygrywa!")
            return True, "Owce wygrywają!"
        elif self.is_blocked():
            print("")
            return True, "Owce zablokowały wilka. Koniec gry!"

        return False, "Gra trwa."

    def is_wolf_winner(self): #czy wilk dotarł do ostatniej kolumny
        row, col = self.wolf.get_position()
        wolf_winner = col == 7

        return wolf_winner

    def is_sheep_winner(self): #czy owce dotarły do pierwszej kolumny
        sheep_winner = all(sheep.get_position()[1] == 0 for sheep in self.sheep)

        return sheep_winner

    def is_blocked(self): #czy wilk jest zablokowany przez owce
        row, col = self.wolf.get_position()
        blocked_condition = all(
            sheep.get_position() == (row - 1, col) or sheep.get_position() == (row + 1, col)
            for sheep in self.sheep)

        return blocked_condition

if __name__ == "__main__":
    player1 = player("Player 1")
    player2 = player2("Player 2")
    session = "session_id"
    game = Game(player1, player2, session)