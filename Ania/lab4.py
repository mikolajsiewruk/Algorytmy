from random import randint
import time as tm
import matplotlib.pyplot as plt
import tabulate as tbl
import pandas as pd
from tabulate import tabulate

class Wyniki:
    def __init__(self, czas_wektory):
        super().__init__()
        self.czas_wektory=czas_wektory
        self.czas_50 = []
        self.czas_100 = []
        self.czas_200 = []
        self.czas_500 = []
        self.czas_1000 = []
        self.czas_2000 = []
        self.mins=[]
        self.maxs=[]
        self.means=[]
        self.oddzielne_wektory()
        self.stat_sort()

    # metoda do wydobycia danych o czasie sortowania wektora o określonym rozmiarze
    def oddzielne_wektory(self):
        for i in range(0,len(self.czas_wektory)):
            self.czas_50.append(self.czas_wektory[i][0])
            self.czas_100.append(self.czas_wektory[i][1])
            self.czas_200.append(self.czas_wektory[i][2])
            self.czas_500.append(self.czas_wektory[i][3])
            self.czas_1000.append(self.czas_wektory[i][4])
            self.czas_2000.append(self.czas_wektory[i][5])

    # metoda licząca statystyki w każdej z wydzielonych wcześniej tabel
    def stat_sort(self):
        args=[self.czas_50,self.czas_100,self.czas_200,self.czas_500,self.czas_1000,self.czas_2000]

        # pętla dla każdej z tabel liczy jej statystyki i dodaje do tabeli statycstycznych
        for wektory in args:
            self.mins.append(min(wektory))
            self.maxs.append(max(wektory))
            self.means.append(sum(wektory)/len(wektory))
class Sorter:
    def __init__(self):
        self.merge_sorted=[]
        self.counting_sorted=[]
        self.quicksorted=[]

    def merge_sort(self, wektor):
        if len(wektor)>1:
            srodek=(len(wektor) // 2) #wyznaczanie środka wektora
            lewa = wektor[:srodek] # podzielenie wektora na część lewą i prawą
            prawa = wektor[srodek:]
            self.merge_sort(lewa) # rekurencyjne wywoływanie dla każdej połowy
            self.merge_sort(prawa)

            i=j=k=0 # początkowe indeksy tablic

            while i < len(lewa) and j < len(prawa):
                # porównywanie elementów lewej i prawej części wektora
                if lewa[i] < prawa[j]: # jezeli elemeny jest mniejszy w części lewej to umieszczamy go w tablicy docelowej
                    wektor[k] = lewa[i]
                    i += 1 # zwiększamy indeks tablicy lewej części
                else:
                    wektor[k] = prawa[j]
                    j += 1 # zwiększamy indeks tablicy prawej części
                k += 1 # zwiększamy indeks tablicy docelowej

            # kopiowanie pozostałych elementów z obu części
            while i < len(lewa):
                wektor[k] = lewa[i]
                i += 1
                k += 1

            while j < len(prawa):
                wektor[k] = prawa[j]
                j += 1
                k += 1
        return wektor

    def counting_sort(self, wektor):
        maks=max(wektor) # znalezienie największej weartości w wektorze
        mini=min(wektor) # znalezienie najmniejszej weartości w wektorze
        posort=[] # tablica na posortowane elementy
        k=[0]*(maks+1) # lista zer, jej długość jest ustalana na podstawie maksymalnej wartości w wektorze zwiększonej o 1
        for i in range(len(wektor)): #przechodzenie przez całą długość wektora
            k[wektor[i]]= k[wektor[i]] + 1 # zwiększenie liczby wystąpień danego elementu wektora tablizy z zeramo o 1
        for j in range(len(k)): # przechodzimy przez listę zer
            if k[j]!=0: # jeżeli element j jest różny od 0, to dodajemy go do posortowanej części
                posort.append(j)
        return posort

    def quick_sort(self, wektor): #zaczęte
        if len(wektor)>1:
            pivot = wektor[-2]
            l = 0
            r = len(wektor) - 1
            while l < r:
                if wektor[l] > pivot and wektor[r] < pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                elif wektor[l] == pivot and wektor[r] < pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                    l += 1
                elif wektor[r] == pivot and wektor[l] > pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                    r -= 1
                elif wektor[l] >= pivot:
                    r -= 1
                elif wektor[r] <= pivot:
                    l += 1
                else:
                    l += 1
                    r -= 1
            c = wektor.count(pivot)
            left = wektor[:wektor.index(pivot) + c]
            right = wektor[wektor.index(pivot) + c:]
            if not left or not right:
                wektor = left + right
                return wektor
            a = self.quick_sort(left)
            b = self.quick_sort(right)
            wektor = a + b
        return wektor

def generowanie_wektorow():
    merge_wektory = []
    counting_wektory = []
    quick_wektory = []
    for i in range(0, len(rozmiary)):
        temporary = [randint(0, 5000) for _ in range(0, rozmiary[i])]
        merge_wektory.append(temporary.copy())
        counting_wektory.append(temporary.copy())
        quick_wektory.append(temporary.copy())
    return merge_wektory,counting_wektory,quick_wektory

merge_czas = []
counting_czas = []
quick_czas = []
rozmiary = [50, 100, 200, 500, 1000, 2000]
sorter=Sorter()

# 100 krotne powtórzenie sortowań (Metoda Monte Carlo)
for i in range(0,10):
    merge_wektory, counting_wektory, quick_wektory = generowanie_wektorow()
    m_temp = []
    c_temp = []
    q_temp = []
    for j in range(6):
        m_start = tm.perf_counter_ns()
        sorter.merge_sort(merge_wektory[j])
        m_end = tm.perf_counter_ns()
        m_temp.append(m_end - m_start)

        c_start = tm.perf_counter_ns()
        sorter.counting_sort(counting_wektory[j])
        c_end = tm.perf_counter_ns()
        c_temp.append(c_end - c_start)

        q_start = tm.perf_counter_ns()
        sorter.quick_sort(quick_wektory[j])
        q_end = tm.perf_counter_ns()
        q_temp.append(q_end - q_start)

    merge_czas.append(m_temp)
    counting_czas.append(c_temp)
    quick_czas.append(q_temp)


# inicjalizacja klasy Results dla wszystkich sortowań, ważne, żeby podać czasy! Klasa sama wyznaczy sobie już wszystko, chillerka :)
merge=Wyniki(merge_czas)
counting=Wyniki(counting_czas)
quick=Wyniki(quick_czas)

plt.figure(1)
plt.plot(rozmiary, merge.means, label="Merge sort średni czas")
plt.plot(rozmiary, counting.means, label="Counting sort średni czas")
plt.plot(rozmiary, quick.means, label="Quick sort średni czas")
plt.title("Średni czas algorytmów sortujących")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(rozmiary, merge.mins, label="min", s=10)
plt.scatter(rozmiary, merge.maxs, label="max", s=10)
plt.scatter(rozmiary, merge.means, label="śr", s=10)
plt.title("Statystyki merge sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(rozmiary, counting.mins, label="min", s=10)
plt.scatter(rozmiary, counting.maxs, label="max", s=10)
plt.scatter(rozmiary, counting.means, label="śr", s=10)
plt.title("Statystyki counting sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(rozmiary, quick.mins, label="min", s=10)
plt.scatter(rozmiary, quick.maxs, label="max", s=10)
plt.scatter(rozmiary, quick.means, label="śr", s=10)
plt.title("Statystyki quick sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.show()

tabela = {
    "Rozmiary": rozmiary,
    "Merge sort [ns]": [merge.means, merge.mins, merge.maxs],
    "Counting sort [ns]": [counting.means, counting.mins, counting.maxs],
    "Quick sort [ns]": [quick.means, quick.mins, quick.maxs]
}

df = pd.DataFrame(tabela)
print(df)


