import random as rnd
import time as tm

def losowanie(N, min_w, max_w):
    return [rnd.randint(min_w, max_w) for _ in range(N)]

def sortowanie_babelkowe(wektor):
    start = tm.perf_counter_ns()
    n = len(wektor)
    for i in range(n):
        for j in range(len(wektor) - 1 - i):
            if wektor[j] > wektor[j + 1]:
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
    stop = tm.perf_counter_ns()
    return stop - start

def insertion(wektor):
    start = tm.perf_counter_ns()
    for i in range(1, len(wektor)):
        j = i - 1
        while j >= 0 and wektor[j] > wektor[j + 1]:
            wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
            j -= 1
    stop = tm.perf_counter_ns()
    return stop - start

def selection(wektor):
    start = tm.perf_counter_ns()
    for i in range(len(wektor)):
        min_i = i
        for j in range(i, len(wektor)):
            if wektor[min_i] > wektor[j]:
                min_i = j
        wektor[min_i], wektor[i] = wektor[i], wektor[min_i]
    stop = tm.perf_counter_ns()
    return stop - start

def test_sortowania():
    długosci_wektorow = [50, 100, 200, 500, 1000, 2000]
    min_w = 0
    max_w = 100
    liczba_powtorzen = 10 #powinno byc 100 ale za długo trwa

    czasy_realizacji = {'Sortowanie bąbelkowe': {},
                        'Sortowanie przez wstawianie': {},
                        'Sortowanie przez wybieranie': {}
                       }

    for dlugosc in długosci_wektorow:
        czasy_babelkowe = []
        czasy_wstawianie = []
        czasy_wybieranie = []

        for _ in range(liczba_powtorzen):
            wektor = losowanie(dlugosc, min_w, max_w)

            czas_babelkowe = sortowanie_babelkowe(wektor.copy())
            czas_wstawianie = insertion(wektor.copy())
            czas_wybieranie = selection(wektor.copy())

            czasy_babelkowe.append(czas_babelkowe)
            czasy_wstawianie.append(czas_wstawianie)
            czasy_wybieranie.append(czas_wybieranie)

        czasy_realizacji['Sortowanie bąbelkowe'][dlugosc] = {
            'Minimalny czas': min(czasy_babelkowe),
            'Średni czas': sum(czasy_babelkowe) / liczba_powtorzen,
            'Maksymalny czas': max(czasy_babelkowe)
        }
        czasy_realizacji['Sortowanie przez wstawianie'][dlugosc] = {
            'Minimalny czas': min(czasy_wstawianie),
            'Średni czas': sum(czasy_wstawianie) / liczba_powtorzen,
            'Maksymalny czas': max(czasy_wstawianie)
        }
        czasy_realizacji['Sortowanie przez wybieranie'][dlugosc] = {
            'Minimalny czas': min(czasy_wybieranie),
            'Średni czas': sum(czasy_wybieranie) / liczba_powtorzen,
            'Maksymalny czas': max(czasy_wybieranie)
        }

    return czasy_realizacji

wyniki = test_sortowania()

print("Minimalny, średni i maksymalny czas realizacji dla każdego algorytmu i dla każdej długości wektora:")

for algorytm in wyniki:
    print(algorytm + ":")
    for dlugosc in wyniki[algorytm]:
        statystyki = wyniki[algorytm][dlugosc]
        print(f"Długość wektora: {dlugosc}")
        print(f"Minimalny czas: {statystyki['Minimalny czas']} ns")
        print(f"Średni czas: {statystyki['Średni czas']} ns")
        print(f"Maksymalny czas: {statystyki['Maksymalny czas']} ns")
    print()
