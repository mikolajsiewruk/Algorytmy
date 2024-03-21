import random as rnd
import time as tm
import matplotlib.pyplot as plt

def losowanie(N, min_w, max_w):
    return [rnd.randint(min_w, max_w) for _ in range(N)]

def sortowanie_babelkowe(wektor):
    n = len(wektor)
    for i in range(n):
        for j in range(len(wektor) - 1 - i):
            if wektor[j] > wektor[j + 1]:
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]

def insertion(wektor):
    for i in range(1, len(wektor)):
        j = i - 1
        while j >= 0 and wektor[j] > wektor[j + 1]:
            wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
            j -= 1

def selection(wektor):
    for i in range(len(wektor)):
        min_i = i
        for j in range(i, len(wektor)):
            if wektor[min_i] > wektor[j]:
                min_i = j
        wektor[min_i], wektor[i] = wektor[i], wektor[min_i]

def test_sortowania(N, liczba_powtorzen):
    długosci_wektorow = [50, 100, 200, 500, 1000, 2000]
    min_w = 0
    max_w = 100

    czasy_babelkowe = {'Minimalny czas': [], 'Średni czas': [], 'Maksymalny czas': []}
    czasy_wstawianie = {'Minimalny czas': [], 'Średni czas': [], 'Maksymalny czas': []}
    czasy_wybieranie = {'Minimalny czas': [], 'Średni czas': [], 'Maksymalny czas': []}

    for dlugosc in długosci_wektorow:
        czasy_babelkowe_dlugosc = []
        czasy_wstawianie_dlugosc = []
        czasy_wybieranie_dlugosc = []

        for _ in range(liczba_powtorzen):
            wektor = losowanie(dlugosc, min_w, max_w)

            start = tm.perf_counter()
            sortowanie_babelkowe(wektor.copy())
            czas_babelkowe = tm.perf_counter() - start
            czasy_babelkowe_dlugosc.append(czas_babelkowe)

            start = tm.perf_counter()
            insertion(wektor.copy())
            czas_wstawianie = tm.perf_counter() - start
            czasy_wstawianie_dlugosc.append(czas_wstawianie)

            start = tm.perf_counter()
            selection(wektor.copy())
            czas_wybieranie = tm.perf_counter() - start
            czasy_wybieranie_dlugosc.append(czas_wybieranie)

        czasy_babelkowe['Minimalny czas'].append(min(czasy_babelkowe_dlugosc))
        czasy_babelkowe['Średni czas'].append(sum(czasy_babelkowe_dlugosc) / liczba_powtorzen)
        czasy_babelkowe['Maksymalny czas'].append(max(czasy_babelkowe_dlugosc))

        czasy_wstawianie['Minimalny czas'].append(min(czasy_wstawianie_dlugosc))
        czasy_wstawianie['Średni czas'].append(sum(czasy_wstawianie_dlugosc) / liczba_powtorzen)
        czasy_wstawianie['Maksymalny czas'].append(max(czasy_wstawianie_dlugosc))

        czasy_wybieranie['Minimalny czas'].append(min(czasy_wybieranie_dlugosc))
        czasy_wybieranie['Średni czas'].append(sum(czasy_wybieranie_dlugosc) / liczba_powtorzen)
        czasy_wybieranie['Maksymalny czas'].append(max(czasy_wybieranie_dlugosc))

    return długosci_wektorow, czasy_babelkowe, czasy_wstawianie, czasy_wybieranie

N = 2000
liczba_powtorzen = 10 #powinno byc 10

długosci_wektorow, czasy_babelkowe, czasy_wstawianie, czasy_wybieranie = test_sortowania(N, liczba_powtorzen)

plt.figure(figsize=(10, 6))
plt.plot(długosci_wektorow, czasy_babelkowe['Średni czas'], label='Sortowanie bąbelkowe')
plt.plot(długosci_wektorow, czasy_wstawianie['Średni czas'], label='Sortowanie przez wstawianie')
plt.plot(długosci_wektorow, czasy_wybieranie['Średni czas'], label='Sortowanie przez wybieranie')
plt.xlabel('Długość wektora')
plt.ylabel('Średni czas realizacji[s]')
plt.title('Średni czas realizacji algorytmów sortowania w zależności od długości wektora')
plt.grid(True)
plt.legend()
plt.show()

# Wykres dla algorytmu sortowania bąbelkowego
plt.figure(figsize=(10, 6))
plt.plot(długosci_wektorow, czasy_babelkowe['Minimalny czas'], label='Minimalny czas')
plt.plot(długosci_wektorow, czasy_babelkowe['Średni czas'], label='Średni czas')
plt.plot(długosci_wektorow, czasy_babelkowe['Maksymalny czas'], label='Maksymalny czas')
plt.xlabel('Długość wektora')
plt.ylabel('Czas realizacji[s]')
plt.title('Algorytm sortowania bąbelkowego')
plt.grid(True)
plt.legend()
plt.show()

# Wykres dla algorytmu sortowania przez wstawianie
plt.figure(figsize=(10, 6))
plt.plot(długosci_wektorow, czasy_wstawianie['Minimalny czas'], label='Minimalny czas')
plt.plot(długosci_wektorow, czasy_wstawianie['Średni czas'], label='Średni czas')
plt.plot(długosci_wektorow, czasy_wstawianie['Maksymalny czas'], label='Maksymalny czas')
plt.xlabel('Długość wektora')
plt.ylabel('Czas realizacji[s]')
plt.title('Algorytm sortowania przez wstawianie')
plt.grid(True)
plt.legend()
plt.show()

# Wykres dla algorytmu sortowania przez wybieranie
plt.figure(figsize=(10, 6))
plt.plot(długosci_wektorow, czasy_wybieranie['Minimalny czas'], label='Minimalny czas')
plt.plot(długosci_wektorow, czasy_wybieranie['Średni czas'], label='Średni czas')
plt.plot(długosci_wektorow, czasy_wybieranie['Maksymalny czas'], label='Maksymalny czas')
plt.xlabel('Długość wektora')
plt.ylabel('Czas realizacji[s]')
plt.title('Algorytm sortowania przez wybieranie')
plt.grid(True)
plt.legend()
plt.show()
