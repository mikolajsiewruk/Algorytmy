from random import randint
import time as tm
import matplotlib.pyplot as plt

class Results:
    def __init__(self, czas_wektory):
        super().__init__()
        self.czas_wektory = czas_wektory
        self.czas50 = []
        self.czas100 = []
        self.czas200 = []
        self.czas500 = []
        self.czas1000 = []
        self.czas2000 = []
        self.min = []
        self.max = []
        self.mean = []
        self.oddziel()
        self.statystyki()

    def oddziel(self):
        for czas in self.czas_wektory:
            self.czas50.append(czas[0])
            self.czas100.append(czas[1])
            self.czas200.append(czas[2])
            self.czas500.append(czas[3])
            self.czas1000.append(czas[4])
            self.czas2000.append(czas[5])

    def statystyki(self):
        realizacja=[self.czas50,self.czas100,self.czas200,self.czas500,self.czas1000,self.czas2000]
        for wektor in realizacja:
            self.min.append(min(wektor))
            self.max.append(max(wektor))
            self.mean.append(sum(wektor)/len(wektor))


def sortowanie_babelkowe(tablica): #algorytm sortowania babelkowego
    start = tm.perf_counter_ns()
    n = len(tablica) #długosc tablicy
    zamiana = False
    for l in range(n-1):
        for i in range(0,n-l-1):
            if tablica[i]>tablica[i+1]: #jesli dwie sasiednie liczby stoja w zlej kolejnosci
                zamiana = True #to zamien miejscami
                tablica[i],tablica[i+1] = tablica[i+1],tablica[i]
    if not zamiana:
        return
    stop = tm.perf_counter_ns()
    czas_sortowanie_babelkowe = stop - start
    return czas_sortowanie_babelkowe

def selection_sort(tablica): #algorytm sortowania przez wybor
    start = tm.perf_counter_ns()
    for i in range(len(tablica)):
        indeks = i
        for j in range(i + 1, len(tablica)):
            if tablica[j] < tablica[indeks]: #jesli  spelnione to znaleziono mniejsza wartosc i sie ja przesuwa
                indeks = j
            tablica[i], tablica[indeks] = tablica[indeks], tablica[i]
        stop = tm.perf_counter_ns()
    czas_selection_sort = stop - start
    return czas_selection_sort

def insertion_sort(tablica): #algorytm sortowania przez wstawianie
    start = tm.perf_counter_ns()
    for i in range(1, len(tablica)): #rozpoczyna od elementu 1
        sprawdzanie = tablica[i]
        indeks = i - 1
        while indeks >= 0 and sprawdzanie < tablica[indeks]:
            tablica[indeks + 1] = tablica[indeks] #przesuwa elementy i ulokowuje sprawdzany indeks
            indeks -= 1
        tablica[indeks + 1] = sprawdzanie
    stop = tm.perf_counter_ns()
    czas_insertion_sort = stop - start
    return czas_insertion_sort


def generator_wektora(sizes):
    babelkowe_wektor = []
    insertion_wektor = []
    selection_wektor = []
    for i in range(0, len(sizes)):
        temporary = [randint(0, 10) for _ in range(0, sizes[i])] #generowanie liczb losowo
        babelkowe_wektor.append(temporary.copy())#dodawanie losowo wygenerowanych liczb do list
        insertion_wektor.append(temporary.copy())
        selection_wektor.append(temporary.copy())
    return babelkowe_wektor,insertion_wektor,selection_wektor

babelkowe_czas = []  # przechowanie czasów sortowań
insertion_czas = []
selection_czas = []
sizes = [50, 100, 200, 500, 1000, 2000]  # rozmiary wektorów

for _ in range(100):
    babelkowe_wektor,insertion_wektor,selection_wektor=generator_wektora(sizes)
    babelkowe_czas.append([sortowanie_babelkowe(babelkowe_wektor[i]) for i in range(len(sizes))]) # w każdej iteracji do tabeli czasów dodawane są kolejne czasy sortowania dla każdego rozmiaru tabeli wejściowej
    insertion_czas.append([insertion_sort(insertion_wektor[i]) for i in range(len(sizes))])
    selection_czas.append([selection_sort(selection_wektor[i]) for i in range(len(sizes))])

bablowe=Results(babelkowe_czas)
insertion=Results(insertion_czas)
selection=Results(selection_czas)


plt.figure(1)
plt.plot(sizes,bablowe.mean,label="Bubble sort srednia")
plt.plot(sizes,insertion.mean,label="Insertion sort srednia")
plt.plot(sizes,selection.mean,label="Selection sort srednia")
plt.title("Sredni czas sortowania algorytmow")
plt.xlabel("rozmiar wektora")
plt.ylabel("czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(sizes,bablowe.min,label="min",s=10)
plt.scatter(sizes,bablowe.max,label="max",s=10)
plt.scatter(sizes,bablowe.mean,label="srednia",s=10)
plt.title("Sortowanie babelkowe")
plt.xlabel("rozmiar wektora")
plt.ylabel("czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(sizes,insertion.min,label="min",s=10)
plt.scatter(sizes,insertion.max,label="max",s=10)
plt.scatter(sizes,insertion.mean,label="srednia",s=10)
plt.title("Insertion sort")
plt.xlabel("rozmiar wektora")
plt.ylabel("czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(sizes,selection.min,label="min",s=10)
plt.scatter(sizes,selection.max,label="max",s=10)
plt.scatter(sizes,selection.mean,label="srednia",s=10)
plt.title("Selection sort")
plt.xlabel("rozmiar wektora")
plt.ylabel("czas sortowania")
plt.legend()
plt.grid(True)

plt.show()
