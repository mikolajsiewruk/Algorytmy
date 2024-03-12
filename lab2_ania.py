import random as rnd
import time as tm
import matplotlib.pyplot as plt
import tabulate as tbl
import numpy as np
import copy as copy


def generowanie_wektora(N, min, max):
    return [rnd.randint(min,max) for i in range(N)]

N = 5
min=0
max=10
wektor_podany=generowanie_wektora(N, min, max)
print(wektor_podany)

N=int(input("Podaj długość wektora: "))
min=int(input("Podaj minimalną wartość wektora: "))
max=int(input("Podaj maksymalną wartość wektora: "))
wektor=generowanie_wektora(N,min,max)
wektor1=wektor.copy()
wektor2=wektor.copy()
wektor3=wektor.copy()
print(wektor)

def bubble_sort(wektor1):
    start:int =tm.perf_counter_ns()
    l=len(wektor1) #długość wektora
    zamiana=False
    for i in range(l-1): #Idziemy przez wektor od początku do przedostatniego elementu
                         #ostatni element pomijamy, bo nie ma go z czym porównać
        for j in range(0, l-i-1): #przechodzimy przez sąsiednie pary elementów
            if wektor1[j]>wektor1[j+1]: #sprawdzamy czy element po lewej jest większy od tego po prawej
                zamiana=True #jeżeli tak następuje zamiana miejsc
                wektor1[j], wektor1[j+1] = wektor1[j+1], wektor1[j]
    if not zamiana: #jeżeli nie nastąpiła żadna zamiana to lista została posortowana
        return
    end = tm.perf_counter_ns()
    czas_bubble_sort=end-start
    return czas_bubble_sort
bubble_sort(wektor1)

print("Wektor posortowany przy użyciu sortowania bąbelkowego: ", wektor1)
print("Czas sortowania:", tm.perf_counter_ns(), "nanosekund")
def selection_sort(wektor2):
    start = tm.perf_counter_ns()
    l=len(wektor2)
    for i in range (l):
        min_el=wektor2[i]  #przypisanie że pierwszy indeks ma wartość element o najmniejszej wartość
        for j in range (i+1, l):
            if wektor2[j]<wektor2[i]: #sprawdzamy czy kolejny element jest mniejszy od naszego min_el
                min_el=j
                wektor2[i], wektor2[min_el]=wektor2[min_el], wektor2[i] # jeżeli tak, nastepuje zamiana miejsc

    end = tm.perf_counter_ns()

    czas_sel_sort=end-start
    return czas_sel_sort

selection_sort(wektor2)
print("Wektor posortowany przy użyciu sortowania poprzez wybór: ", wektor2)
print("Czas sortowania:", tm.perf_counter_ns(), "nanosekund")

def insertion_sort(wektor3):
    start=tm.perf_counter_ns()
    l=len(wektor3)
    for j in range(1, l):
        element=wektor3[j]
        i=j-1 #poprzedni wyraz wektora
        while i>=0 and element< wektor3[i]: #jeżeli i>=0 i zadeklarowany element jest mniejszy od wyrazu z posorotwanej części
            wektor3[i+1]=wektor3[i] #to dodaje element do posortowanej części
            i=i-1 #zmniejszamy długość wektora
        wektor3[i+1]=element #jeżeli warunek niespełniony, to DOPYTAĆ O CHUJ CHODZI
    end=tm.perf_counter_ns()
    czas_ins_sort=end-start
    return czas_ins_sort
insertion_sort(wektor3)
print("Wektor posortowany przy użyciu sortowania przez wstawianie: ", wektor3)
print("Czas sortowania:", tm.perf_counter_ns(), "nanosekund")


def rysowanie_wykresu():
    plt.plot(N, czas_bubble_sort, label="Bubble sort")
    plt.plot(N, czas_sel_sort, label="Insertion sort")
    plt.plot(N, czas_ins_sort, label="Selection sort")
    plt.xlabel('Rozmiar wektora')
    plt.ylabel('Runtime (ns)')
    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
a=rysowanie_wykresu()
print(a)
