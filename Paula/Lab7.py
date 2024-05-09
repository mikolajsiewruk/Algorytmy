from tabulate import tabulate
import heapq
from collections import Counter, defaultdict
import time
import matplotlib.pyplot as plt
class Węzeł:
    def __init__(self, symbol=None, częstość=None):
        self.symbol = symbol
        self.częstość = częstość
        self.lewe = None
        self.prawe = None
    def __lt__(self, other):
        return self.częstość < other.częstość
def zlicz_częstość(tekst):
    return Counter(tekst)
def zbuduj_drzewo_huffmana(mapa_częstości):
    kolejka_priorytetowa = [Węzeł(symbol, częstość) for symbol, częstość in mapa_częstości.items()]
    heapq.heapify(kolejka_priorytetowa)
    while len(kolejka_priorytetowa) > 1:
        lewe = heapq.heappop(kolejka_priorytetowa)
        prawe = heapq.heappop(kolejka_priorytetowa)
        połączony = Węzeł(częstość=lewe.częstość + prawe.częstość)
        połączony.lewe = lewe
        połączony.prawe = prawe
        heapq.heappush(kolejka_priorytetowa, połączony)
    return kolejka_priorytetowa[0]


def generuj_kody_huffmana(węzeł, kod='', mapa_kodów=None):
    if mapa_kodów is None:
        mapa_kodów = {}
    if węzeł.symbol is not None:
        mapa_kodów[węzeł.symbol] = kod
    else:
        generuj_kody_huffmana(węzeł.lewe, kod + '0', mapa_kodów)
        generuj_kody_huffmana(węzeł.prawe, kod + '1', mapa_kodów)
    return mapa_kodów


def zakoduj(tekst, mapa_kodów):
    zakodowany_tekst = ''
    for znak in tekst:
        zakodowany_tekst += mapa_kodów[znak]
    return zakodowany_tekst


def odkoduj(zakodowany_tekst, drzewo_huffmana):
    odkodowany_tekst = ''
    aktualny_węzeł = drzewo_huffmana
    for bit in zakodowany_tekst:
        if bit == '0':
            aktualny_węzeł = aktualny_węzeł.lewe
        else:
            aktualny_węzeł = aktualny_węzeł.prawe

        if aktualny_węzeł.symbol is not None:
            odkodowany_tekst += aktualny_węzeł.symbol
            aktualny_węzeł = drzewo_huffmana
    return odkodowany_tekst


def wygeneruj_tabelę(mapa_kodów, mapa_częstości):
    tabela = [["Symbol", "Liczność", "Kod Huffmana"]]
    for symbol, częstość in mapa_częstości.items():
        kod = mapa_kodów[symbol]
        tabela.append([symbol, częstość, kod])
    return tabela


if __name__ == "__main__":
    tekst = "Lorem ipsum dolor sit amet."

    # Zliczanie częstości symboli
    mapa_częstości = zlicz_częstość(tekst)

    # Budowanie drzewa Huffmana
    drzewo_huffmana = zbuduj_drzewo_huffmana(mapa_częstości)

    # Generowanie kodów Huffmana
    mapa_kodów = generuj_kody_huffmana(drzewo_huffmana)

    # Kompresja tekstu
    zakodowany_tekst = zakoduj(tekst, mapa_kodów)

    # Dekompresja tekstu
    odkodowany_tekst = odkoduj(zakodowany_tekst, drzewo_huffmana)

    # Wygenerowanie tabeli
    tabela = wygeneruj_tabelę(mapa_kodów, mapa_częstości)

    # Wyświetlenie tabeli
    print(tabulate(tabela, headers="firstrow", tablefmt="grid"))

    # Wyświetlenie zakodowanego tekstu
    print("\nZakodowany tekst:", zakodowany_tekst)

    # Wyświetlenie zdekodowanego tekstu
    print("\nZdekodowany tekst:", odkodowany_tekst)


    def pobierz_n_wersow(n, nazwa_pliku='dane.txt'):
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            wersy = [next(plik) for _ in range(n)]
        return ''.join(wersy)


    if __name__ == "__main__":
        # Lista zawierająca liczby wersów do pobrania
        liczba_wersow = [1, 3, 10, 25, 50]

        for n in liczba_wersow:
            # Pobranie n wersów z pliku
            tekst = pobierz_n_wersow(n)

            # Wyświetlenie ilości znaków przed kompresją
            print(f"\nIlość znaków przed kompresją ({n} wersów): {len(tekst)}")

            # Kompresja tekstu
            mapa_częstości = zlicz_częstość(tekst)
            drzewo_huffmana = zbuduj_drzewo_huffmana(mapa_częstości)
            mapa_kodów = generuj_kody_huffmana(drzewo_huffmana)
            zakodowany_tekst = zakoduj(tekst, mapa_kodów)

            # Wyświetlenie ilości bitów po kompresji
            print(f"Ilość bitów po kompresji ({n} wersów): {len(zakodowany_tekst)}")

            # Dekompresja tekstu
            odkodowany_tekst = odkoduj(zakodowany_tekst, drzewo_huffmana)

            # Sprawdzenie, czy dekompresowany tekst jest zgodny z oryginałem
            if odkodowany_tekst == tekst:
                print(f"Dekompresja poprawna ({n} wersów)")
            else:
                print(f"Błąd dekompresji ({n} wersów)")

# Listy przechowujące dane
liczba_znakow_przed_kompresja = []
liczba_bitow_po_kompresji = []
czas_kompresji = []
czas_dekompresji = []
poziom_kompresji = []

# Iteracja po różnych ilościach znaków w tekście
for n in liczba_wersow:
    tekst = pobierz_n_wersow(n)

    # Zliczanie liczby znaków przed kompresją
    liczba_znakow_przed_kompresja.append(len(tekst))

    start_kompresji = time.time()
    mapa_częstości = zlicz_częstość(tekst)
    drzewo_huffmana = zbuduj_drzewo_huffmana(mapa_częstości)
    mapa_kodów = generuj_kody_huffmana(drzewo_huffmana)
    zakodowany_tekst = zakoduj(tekst, mapa_kodów)
    end_kompresji = time.time()

    # Zliczanie liczby bitów po kompresji
    liczba_bitow_po_kompresji.append(len(zakodowany_tekst))

    start_dekompresji = time.time()
    odkodowany_tekst = odkoduj(zakodowany_tekst, drzewo_huffmana)
    end_dekompresji = time.time()

    czas_kompresji.append(end_kompresji - start_kompresji)
    czas_dekompresji.append(end_dekompresji - start_dekompresji)
    poziom_kompresji.append(len(zakodowany_tekst) / len(tekst))

# Generowanie wykresów
plt.figure(figsize=(15, 5))

# Wykres liczby bitów przed i po kompresji
plt.subplot(1, 3, 1)
plt.plot(liczba_znakow_przed_kompresja, liczba_znakow_przed_kompresja, label='Po kompresji')
plt.plot(liczba_znakow_przed_kompresja, liczba_bitow_po_kompresji, label='Przed kompresją')
plt.xlabel('Liczba znaków')
plt.ylabel('Liczba bitów')
plt.title('Liczba bitów przed i po kompresji')
plt.legend()

# Wykres czasu kompresji i dekompresji
plt.subplot(1, 3, 2)
plt.plot(liczba_znakow_przed_kompresja, czas_kompresji, label='Kompresja')
plt.plot(liczba_znakow_przed_kompresja, czas_dekompresji, label='Dekompresja')
plt.xlabel('Liczba znaków')
plt.ylabel('Czas [s]')
plt.title('Czas kompresji i dekompresji')
plt.legend()

# Wykres poziomu kompresji
plt.subplot(1, 3, 3)
plt.plot(liczba_znakow_przed_kompresja, poziom_kompresji)
plt.xlabel('Liczba znaków')
plt.ylabel('Poziom kompresji')
plt.title('Poziom kompresji')

plt.tight_layout()
plt.show()