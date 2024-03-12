import random as rnd
import time as tm
import matplotlib.pyplot as plt
import tabulate as tbl
import numpy as np

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
print(wektor)

def bubble_sort(wektor):
    l=len(wektor) #długość wektora
    zamiana=False
    for i in range(l-1): #Idziemy przez wektor od początku do przedostatniego elementu
                         #ostatni element pomijamy, bo nie ma go z czym porównać
        for j in range(0, l-i-1): #przechodzimy przez sąsiednie pary elementów
            if wektor[j]>wektor[j+1]: #sprawdzamy czy element po lewej jest większy od tego po prawej
                zamiana=True #jeżeli tak następuje zamiana miejsc
                wektor[j], wektor[j+1] = wektor[j+1], wektor[j]
    if not zamiana: #jeżeli nie nastąpiła żadna zamiana to lista została posortowana
        return
bubble_sort(wektor)
print("Wektor posortowany przy użyciu sortowania bąbelkowego: ", wektor)

def selection_sort(wektor):
    l=len(wektor)
    for i in range (l):
        min_ind=i  #indeks komórki z najmniejszym elementem
        for j in range (i+1, l):
            if wektor[j]<wektor[i]:
                min_el=j
        wektor[i], wektor[min_el]=wektor[min_el], wektor[i] #zamienia go z następnym elementem listy
selection_sort(wektor)
print("Wektor posortowany przy użyciu sortowania poprzez wybór: ", wektor)