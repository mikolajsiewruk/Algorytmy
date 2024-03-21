import random as rnd
import time as tm


def losowanie(N, min_w, max_w):
    return [rnd.randint(min_w, max_w) for _ in range(N)]


def sortowanie_babelkowe(wektor1):
    start = tm.perf_counter_ns()
    n = len(wektor1)
    for i in range(n):
        for j in range(len(wektor1) - 1 - i):
            if wektor1[j] > wektor1[j + 1]:
                wektor1[j], wektor1[j + 1] = wektor1[j + 1], wektor1[j]
    stop = tm.perf_counter_ns()
    return stop - start


def insertion(wektor1):  # wstawianie
    start = tm.perf_counter_ns()
    for i in range(1, len(wektor1)):
        j = i - 1
        while j >= 0 and wektor1[j] > wektor1[j + 1]:
            wektor1[j], wektor1[j + 1] = wektor1[j + 1], wektor1[j]
            j -= 1
    stop = tm.perf_counter_ns()
    return stop - start


def selection(wektor1):  # wybieranie
    start = tm.perf_counter_ns()
    for i in range(len(wektor1)):
        min_i = i
        for j in range(i, len(wektor1)):
            if wektor1[min_i] > wektor1[j]:
                min_i = j
        wektor1[min_i], wektor1[i] = wektor1[i], wektor1[min_i]
    stop = tm.perf_counter_ns()
    return stop - start


def test_sortowania(N):
    min_w = 0
    max_w = 100

    czasy = {'Sortowanie bąbelkowe[ns]': [],
             'Sortowanie przez wstawianie[ns]': [],
             'Sortowanie przez wybieranie[ns]': []
             }

    for _ in range(N):
        wektor = losowanie(N, min_w, max_w)

        czas_babelkowe = sortowanie_babelkowe(wektor.copy())
        czas_wstawianie = insertion(wektor.copy())
        czas_wybieranie = selection(wektor.copy())

        czasy['Sortowanie bąbelkowe[ns]'].append(czas_babelkowe)
        czasy['Sortowanie przez wstawianie[ns]'].append(czas_wstawianie)
        czasy['Sortowanie przez wybieranie[ns]'].append(czas_wybieranie)

    return czasy


N = int(input("Podaj liczbę N: "))
wyniki = test_sortowania(N)
print("Czasy realizacji dla każdej iteracji dla każdego algorytmu sortowania:")
print(wyniki)
