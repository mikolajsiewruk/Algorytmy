import pygame  # Import biblioteki Pygame
import sys  # Import modułu systemowego

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 560, 560  # Szerokość i wysokość okna gry
ROWS, COLS = 7, 7  # Liczba wierszy i kolumn na planszy
SQUARE_SIZE = WIDTH // COLS  # Rozmiar pojedynczego pola na planszy

# Kolory
WHITE = (255, 255, 255)  # Kolor biały
BLACK = (0, 0, 0)  # Kolor czarny
RED = (255, 0, 0)  # Kolor czerwony
BLUE = (0, 0, 255)  # Kolor niebieski

# Inicjalizacja okna gry
win = pygame.display.set_mode((WIDTH, HEIGHT))  # Utworzenie okna gry o określonych wymiarach
pygame.display.set_caption("Fox and Geese")  # Ustawienie tytułu okna gry

# Inicjalizacja planszy
board = [["." for _ in range(COLS)] for _ in range(ROWS)]  # Utworzenie planszy jako lista dwuwymiarowa z wypełnieniem kropek
board[0][0] = "F"  # Ustawienie lisa na pozycji (0, 0)
for j in range(COLS):
    board[ROWS - 1][j] = "G"  # Ustawienie gęsi na dolnej krawędzi planszy

# Funkcja rysująca planszę
def draw_board():
    win.fill(WHITE)  # Wypełnienie okna kolorem białym
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(win, BLACK, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)  # Narysowanie siatki planszy
            if board[row][col] == "F":
                pygame.draw.circle(win, RED, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//3)  # Narysowanie lisa
            elif board[row][col] == "G":
                pygame.draw.circle(win, BLUE, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//3)  # Narysowanie gęsi
    pygame.display.update()  # Odświeżenie ekranu

# Sprawdzenie, czy ruch jest dozwolony dla lisa
def is_valid_fox_move(start, end):
    start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < ROWS and 0 <= start_col < COLS and 0 <= end_row < ROWS and 0 <= end_col < COLS):
        return False  # Sprawdzenie, czy pole końcowe znajduje się na planszy

    if board[end_row][end_col] != ".":
        return False  # Sprawdzenie, czy pole końcowe jest puste

    if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
        return False  # Sprawdzenie, czy ruch jest na ukos

    return True

# Sprawdzenie, czy ruch jest dozwolony dla gęsi
def is_valid_goose_move(start, end):
    start_row, start_col = start
    end_row, end_col = end

    if not (0 <= start_row < ROWS and 0 <= start_col < COLS and 0 <= end_row < ROWS and 0 <= end_col < COLS):
        return False  # Sprawdzenie, czy pole końcowe znajduje się na planszy

    if board[end_row][end_col] != ".":
        return False  # Sprawdzenie, czy pole końcowe jest puste

    if start_row - end_row != 1 or abs(start_col - end_col) != 1:
        return False  # Sprawdzenie, czy ruch jest na ukos w przód

    return True

# Sprawdzenie, czy lis wygrał
def is_fox_winner():
    for col in range(COLS):
        if board[ROWS - 1][col] == "F":  # Sprawdzenie, czy lis dotarł do dolnej krawędzi planszy
            return True
    return False

# Sprawdzenie, czy gęsi wygrały
def is_goose_winner():
    fox_moves = [(i, j) for i in range(ROWS) for j in range(COLS) if board[i][j] == "F"]  # Pozycje lisa na planszy
    for move in fox_moves:  # Sprawdzamy dostępne ruchy dla lisa
        row, col = move
        if row < ROWS - 1:
            if col > 0 and board[row + 1][col - 1] == "." and board[row][col - 1] != "G":  # Sprawdzenie ruchu na skos w lewo do przodu
                return False
            if col < COLS - 1 and board[row + 1][col + 1] == "." and board[row][col + 1] != "G":  # Sprawdzenie ruchu na skos w prawo do przodu
                return False
        if row > 0:
            if col > 0 and board[row - 1][col - 1] == "." and board[row][col - 1] != "G":  # Sprawdzenie ruchu na skos w lewo do tyłu
                return False
            if col < COLS - 1 and board[row - 1][col + 1] == "." and board[row][col + 1] != "G":  # Sprawdzenie ruchu na skos w prawo do tyłu
                return False
    return True  # Jeśli lis jest zablokowany, gęsi wygrywają

# Główna pętla gry
def main():
    fox_turn = True  # Zmienna śledząca, czy jest kolej lisa
    selected_piece = None  # Wybrany przez gracza pionek
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                if fox_turn:
                    if board[row][col] == "F":
                        selected_piece = (row, col)  # Wybranie lisa
                else:
                    if board[row][col] == "G":
                        selected_piece = (row, col)  # Wybranie gęsi

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                if selected_piece:
                    if fox_turn:
                        if is_valid_fox_move(selected_piece, (row, col)):
                            board[selected_piece[0]][selected_piece[1]] = "."  # Usunięcie lisa z poprzedniej pozycji
                            board[row][col] = "F"  # Przesunięcie lisa na nową pozycję
                            fox_turn = not fox_turn  # Zmiana tury
                    else:
                        if is_valid_goose_move(selected_piece, (row, col)):
                            board[selected_piece[0]][selected_piece[1]] = "."  # Usunięcie gęsi z poprzedniej pozycji
                            board[row][col] = "G"  # Przesunięcie gęsi na nową pozycję
                            fox_turn = not fox_turn  # Zmiana tury

        draw_board()  # Narysowanie aktualnego stanu planszy

        if is_fox_winner():
            print("Fox wins!")  # Wyświetlenie komunikatu o wygranej lisa
            break
        elif is_goose_winner():
            print("Geese win!")  # Wyświetlenie komunikatu o wygranej gęsi
            break

# Uruchomienie gry
if __name__ == "__main__":
    main()
