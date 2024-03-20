import random as rnd
import time as tm
import matplotlib.pyplot as plt
import tabulate as tbl
import pandas as pd

def bubble_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)  # długość wektora
    zamiana = False
    for i in range(l - 1):  # Idziemy przez wektor od początku do przedostatniego elementu
        # ostatni element pomijamy, bo nie ma go z czym porównać
        for j in range(0, l - i - 1):  # przechodzimy przez sąsiednie pary elementów
            if wektor[j] > wektor[j + 1]:  # sprawdzamy czy element po lewej jest większy od tego po prawej
                zamiana = True  # jeżeli tak następuje zamiana miejsc
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
    if not zamiana:  # jeżeli nie nastąpiła żadna zamiana to lista została posortowana
        return
    end = tm.perf_counter_ns()
    czas_bubble_sort = end - start
    return czas_bubble_sort, wektor


def selection_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)
    for i in range(0, l - 1):
        min_ind = 0  #przypisanie że pierwszy indeks ma  element o najmniejszej wartości
        for j in range(i + 1, l):
            if wektor[j] < wektor[min_ind]:  # sprawdzamy czy kolejny element jest mniejszy od naszego min_el
                min_ind = j #jeżeli tak przypisujemy nową wartość min_ind
        wektor[i], wektor[min_ind] = wektor[min_ind], wektor[i]   #i zamieniamy miejscami

    end = tm.perf_counter_ns()
    czas_sel_sort = end - start
    return czas_sel_sort, wektor


def insertion_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)
    for i in range(1, l):
        k = wektor[i]
        ind_posort = i - 1 #odejmjemy 1 aby zrobić miejsce dla nowego elementu
        while k < wektor[ind_posort] and ind_posort >= 0:
            wektor[ind_posort + 1] = wektor[ind_posort] #przesuwanie elementów
            ind_posort = ind_posort - 1
        wektor[ind_posort + 1] = k

    end = tm.perf_counter_ns()
    czas_ins_sort = end - start
    return czas_ins_sort, wektor


bubble_wektory = []
selection_wektory = []
insert_wektory = []
bubble_czas = []
insert_czas = []
selection_czas = []
rozmiary = [50, 100, 200, 500, 1000, 2000]

for i in range(0, len(rozmiary)):
    temporary = [rnd.randint(0, 5000) for _ in range(0, rozmiary[i])]
    bubble_wektory.append(temporary.copy())
    selection_wektory.append(temporary.copy())
    insert_wektory.append(temporary.copy())

bubble_czas = [bubble_sort(bubble_wektory[i])[0] for i in range(0, 6)]
selection_czas = [selection_sort(selection_wektory[i])[0] for i in range(0, 6)]
insert_czas = [insertion_sort(insert_wektory[i])[0] for i in range(0, 6)]


def rysowanie_wykresu():
    plt.plot([50, 100, 200, 1000, 2000, 5000], bubble_czas, label="Sortowanie bombelkowe")
    plt.plot([50, 100, 200, 1000, 2000, 5000], insert_czas, label="Sorotwanie przez wstawianie")
    plt.plot([50, 100, 200, 1000, 2000, 5000], selection_czas, label="Sortowanie przez wybór")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas sortowania [nanosekundy]")
    plt.title("Porównanie czasu sortowania algorytmów")
    plt.legend()
    plt.grid(True)
    plt.show()


rysowanie_wykresu()

tabela={
    "bubble sort": bubble_czas,
    "selection sort": selection_czas,
    "insertion sort": insert_czas
}
df = pd.DataFrame(tabela, index = rozmiary)

print(tbl.tabulate({"Rozmiary": rozmiary,"Bubble sort [ns]": bubble_czas,"Selection sort [ns]": selection_czas,"insertion sort [ns]": insert_czas}, headers="keys", tablefmt="mixed_grid"))
