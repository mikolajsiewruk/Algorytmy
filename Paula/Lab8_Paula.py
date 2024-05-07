from tkinter import *

# Inicjalizacja okna
root = Tk()

# Nadanie tytułu okna
root.title("Kółko i Krzyżyk")

# Ustawienie przezroczystości okna
root.attributes('-alpha', 0.8)

# Zmiana tła okna
root.config(background="light green")

# Wymiary okna
szer_okna = 500
wys_okna = 500

# Znalezienie środka ekranu
srodek_x = int((root.winfo_screenwidth() / 2) - (szer_okna / 2))
srodek_y = int((root.winfo_screenheight() / 2) - (wys_okna / 2))

# Ustawienie wymiarów okna oraz jego pozycji
root.geometry(f'{szer_okna}x{wys_okna}+{srodek_x}+{srodek_y}')

# plansza jako lista
plansza = [[' ' for _ in range(10)] for _ in range(10)]

# Inicjalizacja listy przycisków
przyciski = []

def klikniecie_przycisku(wiersz, kolumna):
    global aktualny_gracz

    if plansza[wiersz][kolumna] == " ":
        plansza[wiersz][kolumna] = aktualny_gracz
        przyciski[wiersz][kolumna].config(text=aktualny_gracz)
        if sprawdz_wygrana(wiersz, kolumna):
            print("Gracz", aktualny_gracz, "wygrał!")
            zablokuj_przyciski()
        elif sprawdz_remis():
            print("Remis!")
            zablokuj_przyciski()
        else:
            aktualny_gracz = "O" if aktualny_gracz == "X" else "X"

def sprawdz_wygrana(wiersz, kolumna):
    aktualny_znak = plansza[wiersz][kolumna]

    # Sprawdzenie wiersza
    if ''.join(plansza[wiersz]).count(aktualny_znak*5) > 0:
        return True

    # Sprawdzenie kolumny
    if ''.join([plansza[i][kolumna] for i in range(10)]).count(aktualny_znak*5) > 0:
        return True

    # Sprawdzenie przekątnych
    if ''.join([plansza[i][i] for i in range(10)]).count(aktualny_znak*5) > 0 or \
       ''.join([plansza[i][9-i] for i in range(10)]).count(aktualny_znak*5) > 0:
        return True

    return False

def sprawdz_remis():
    return all(plansza[i][j] != " " for i in range(10) for j in range(10))

def zablokuj_przyciski():
    for wiersz in przyciski:
        for przycisk in wiersz:
            przycisk.config(state=DISABLED)

aktualny_gracz = "X"

for i in range(10):
    # Inicjalizacja listy przycisków w bieżącym wierszu
    wiersz_przyciskow = []

    for j in range(10):
        # Utworzenie przycisku Button
        przycisk = Button(root,
                          text=" ",
                          font=("Arial", 20),
                          width=2,
                          height=1,
                          command=lambda w=i, k=j: klikniecie_przycisku(w, k))

        # Umieszczenie przycisku w odpowiednim miejscu
        przycisk.grid(row=i, column=j)

        # Dodanie przycisków w bieżącym wierszu do listy przycisków
        wiersz_przyciskow.append(przycisk)

    # Dodanie przycisków w bieżącym wierszu do listy przycisków
    przyciski.append(wiersz_przyciskow)

root.mainloop()
