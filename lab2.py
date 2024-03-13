import random as rnd
import time as tm
import matplotlib.pyplot as plt
import numpy as np

# 3 razy zdefiniowana jest ta funkcja, wystarczy raz a nastepnie sie do niej odwoływać np a=generowanie_wektora(parametry), tak jak jest w kodzie ponizej
# tak samo 2 razy definiowane N min i max, wystarczy raz i bedzie kox
def generator_wektora(N, min, max):  # generuje wektor
    return np.random.randint(min, max, N)


def sortowanie_babelkowe(tablica):
    start= tm.perf_counter_ns()
    n = len(tablica)  # długosc tablicy
    zamiana = False
    for l in range(n - 1):
        for i in range(0, n - l - 1):
            if tablica[i] > tablica[i + 1]:  # jesli dwie sasiednie liczby stoja w zlej kolejnosci
                zamiana = True  # ta? to zamien miejscami
                tablica[i], tablica[i + 1] = tablica[i + 1], tablica[i]
    if not zamiana:
        return tablica
    end= tm.perf_counter_ns()
    return end-start


N = 5
min = 0 # dobra praktyka nie używac nazw funkcji wbudowanych do nazywania zmiennych, MS
max = 10
tablica = generator_wektora(N, min, max)
posortowana = sortowanie_babelkowe(tablica.copy())
print(posortowana)


def generator_wektora(N, min, max):
    return np.random.randint(min, max, N)


def selection_sort(tablica):
    for l in range(0, len(tablica)):
        a = tablica[l]
        index = tablica = tablica.index(min(tablica[l + 1:]))
        tablica[l] = tablica[index]
        tablica = index = a


print(tablica)
print(selection_sort)
N = 5
min = 0
max = 10
tablica = generator_wektora(N, min, max)
posortowana = sortowanie_babelkowe(tablica.copy())
print(posortowana)


def generator_wektora(N, min, max):
    return np.random.randint(min, max, N)


'''def insertion_sort(tablica):
    nie
    zdazylam'''
