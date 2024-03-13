import random as rnd
import time as tm
import matplotlib.pyplot as plt
#import tabulate as tbl
import numpy as np
import copy as copy  # copy to wbudowana metoda tablic nie trzeba jej importowac


def generowanie_wektora(min, max):
    sizes=[50,100,200,1000,2000,5000]
    wektory=[]
    for i in range(0,6):
        wektory.append([rnd.randint(min,max) for i in range(sizes[i])])
    return wektory
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


def selection_sort(arr):
    start = tm.perf_counter_ns()
    for j in range(0, len(arr)):
        top = 0
        for i in range(0, len(arr) - j):
            if arr[i] > top:
                top = arr[i]
        arr[arr.index(top)], arr[-1 - j] = arr[-1 - j], arr[arr.index(top)]
    end = tm.perf_counter_ns()
    return end - start
'''print(generowanie_wektora(10,10000))# usunac
N = 5
min=0 # dobra praktyka nie uzywac nazw funkcji wbudowanych jako nazwy zmiennych, polecam MS
max=10''' # mozna usunac
wektory=generowanie_wektora(10,1000)
w1=wektory.copy()
w2=wektory.copy()
w3=wektory.copy()
print(w1)
print(w2)
print(w3)
czas_bubble=[]
czas_ins=[]
czas_sel=[]
for i in range(0,6):
    czas_bubble.append(bubble_sort(w1[i]))
    czas_ins.append(insertion_sort(w2[i]))
    czas_sel.append(selection_sort(w3[i]))
'''wektor_podany=generowanie_wektora(min, max)
print(wektor_podany)'''
print(czas_ins)
print(czas_sel)
print(czas_bubble)
N=int(input("Podaj długość wektora: "))
min=int(input("Podaj minimalną wartość wektora: "))
max=int(input("Podaj maksymalną wartość wektora: "))
wektor=generowanie_wektora(min,max)
wektor1=wektor.copy()
wektor2=wektor.copy()
wektor3=wektor.copy()
print(wektor)
print(wektor1)
# najpierw funkcje potem zmienne

#czas_bubble_sort=bubble_sort(wektor1)# przypisana zmienna do wartości funkcji

print("Wektor posortowany przy użyciu sortowania bąbelkowego: ", wektor1)
print("Czas sortowania:", "nanosekund") # zamiast tm.perf_couter_ns dalem wartosc czasu bubble sorta itd w kazdym innym


#czas_sel_sort=selection_sort(wektor2) # przypisana zmienna do wartości funkcji
print("Wektor posortowany przy użyciu sortowania poprzez wybór: ", wektor2)
print("Czas sortowania:", "nanosekund")

#czas_ins_sort=insertion_sort(wektor3)
print("Wektor posortowany przy użyciu sortowania przez wstawianie: ", wektor3)
print("Czas sortowania:", "nanosekund")

# zmieniłem wykres tak zeby cokolwiek pokazywał, przy jednej próbie należałoby użyć wykresu puktowego, bo inaczej nic sie nie wyswietla
def rysowanie_wykresu():
    plt.plot([50, 100, 200, 1000, 2000, 5000], czas_ins, label="Insertion sort")
    plt.plot([50,100,200,1000,2000,5000],czas_bubble, label="Bubble sort")
    plt.plot([50,100,200,1000,2000,5000],czas_sel, label="Selection sort")
    plt.xlabel('Rozmiar wektora')
    plt.ylabel('Runtime (ns)')
    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
rysowanie_wykresu()# to nic nie robi
# wykres sie nie rysuje bo N nie jest tabicą rozmiarów prób