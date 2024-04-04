import time as tm
import matplotlib.pyplot as plt
from numpy.random import random


class Results:
    # ważne! tak się deklaruje klasy w python, bardzo przydatne, warto umieć! (napisanie jednej klasy zaoszczędziło mi pisania 100 linijek kodu dla tego zadania)
    def __init__(self,time_arr):
        super().__init__()
        self.time_arr=time_arr
        self.time50 = []
        self.time100 = []
        self.time200 = []
        self.time500 = []
        self.time1000 = []
        self.time2000 = []
        self.mins=[]
        self.maxs=[]
        self.means=[]
        self.separate_arrays()
        self.get_stats()

    # metoda separate arrays służąca do wydobycia danych o czasie sortowania tablicy o określonym rozmiarze, ważne jest,żeby przy inicjalizacji klasy podac wektor wektorów (funkcja generate vectors)
    def separate_arrays(self):
        for i in range(0,len(self.time_arr)):
            self.time50.append(self.time_arr[i][0])
            self.time100.append(self.time_arr[i][1])
            self.time200.append(self.time_arr[i][2])
            self.time500.append(self.time_arr[i][3])
            self.time1000.append(self.time_arr[i][4])
            self.time2000.append(self.time_arr[i][5])

    # metoda licząca statystyki w każdej z wydzielonych wcześniej tabel
    def get_stats(self):
        args=[self.time50,self.time100,self.time200,self.time500,self.time1000,self.time2000]

        # pętla dla każdej z tabel liczy jej statystyki i dodaje do tabeli statycstycznych
        for arr in args:
            self.mins.append(min(arr))
            self.maxs.append(max(arr))
            self.means.append(sum(arr)/len(arr))
def merge_sort(tablica):
    if len(tablica) > 1:  # jesli dlugosc tablicy wieksza niz jeden
        srodek = int(len(tablica) // 2)  # to podziel na 2
    prawa = tablica[srodek:]
    lewa = tablica[:srodek]  # dzieli na czesci lewa od poczatku do srodka prawa od srodka do konca
    merge_sort(lewa)
    merge_sort(prawa)
    p = 0
    t = 0
    l = 0

    while l < len(lewa) and p < len(prawa):  # porównywanie elementów z lewej i z prawej tablicy
        if lewa[l] < prawa[p]:
            tablica[t] = lewa[l]  # jesli lewa jest mniejsza to przypisywany do tablicy
            l = l + 1
        else:
            tablica[t] = prawa[p]  # jesli prawa jest mniejsza to przypisywany do tablicy
            p = l + 1
        t = t + 1  # zwiekszenie indeksu
        while l < len(lewa):  # na niesprawdzone elementy
            tablica[t] = lewa[l]
            l = l + 1
            t = t + 1
        while p < len(prawa):
            tablica[t] = prawa[p]
            p = p + 1
            t = t + 1
    return tablica


def counting_sort(tablica):
    gora = max(tablica)  # wart max
    y = []  # lista na posortowane argumeny
    k = [0] * (gora + 1)  # tablica k o długości ymax - ymin + 1 zawierającą same wartości 0
    for i in range(len(tablica)):
        k[tablica[i]] = k[tablica[
            i]] + 1  # iteruj po każdym elemencie yi z listy y i zwiększ o 1 wartość listy k w indeksie yi − ymin
    for j in range(len(k)):
        if k[j] != 0:  # dodaje indeks do listy wyjsciowej jesli nie jest on rowny 0
            y.append(j)
    return y

def quick_sort(tablica):
    wiekszy = []
    mniejszy = []
    srodkowy = []
    if len(tablica) > 1 : #wiecej niz 1 element - nie jest posortowana
        pivot = tablica[len(tablica) // 2] #wybiera srodkowy element jako pivot
        for x in tablica:
            if x < pivot: #jesli dany x bedzie mniejszy niz pivot
                mniejszy.append(x) #dodaj do listy mniejszy
            elif x == pivot: #jesli dany x bedzie rowny to dodaj do listy rowny
                srodkowy.append(x)
            elif x > pivot:
                wiekszy.append(x) #jesli wiekszy to do listy wiekszy

        a = quick_sort(mniejszy)
        b = quick_sort(wiekszy)
        tab = a + srodkowy + b #zlaczenie list
    return tab

def generate_vector()-> tuple:
    '''
    Generates random vectors with sizes given below

    :return: list of lists containing every vector size for every sorting algorithm
    '''
    sizes = [50, 100, 200, 500, 1000, 2000]
    merge_arrays = []
    counting_arrays = []
    quicksort_arrays = []
    for i in range(0, len(sizes)):
        temporary = [random.randint(0, 5000) for _ in range(0, sizes[i])]
        merge_arrays.append(temporary.copy())
        counting_arrays.append(temporary.copy())
        quicksort_arrays.append(temporary.copy())
    return merge_arrays,counting_arrays,quicksort_arrays

merge_time = []
counting_time = []
quicksort_time = []

sizes = [50, 100, 200, 500, 1000, 2000]
sorter = Sorter()

# 100 krotne powtórzenie sortowań (Metoda Monte Carlo), w instrukcji jest żeby ilość iteracji podawać z klawiatury (nie chce mi sie)
for i in range(0,100):
    merge_arrays, counting_arrays, quicksort_arrays = generate_vector()
    m_temp = []
    c_temp = []
    q_temp = []
    for j in range(6):
        m_start=tm.perf_counter_ns()
        sorter.merge_sort(merge_arrays[j])
        m_end=tm.perf_counter_ns()
        m_temp.append(m_end-m_start)

        c_start = tm.perf_counter_ns()
        sorter.counting_sort(counting_arrays[j])
        c_end = tm.perf_counter_ns()
        c_temp.append(c_end - c_start)

        q_start = tm.perf_counter_ns()
        sorter.quicksort(quicksort_arrays[j])
        q_end = tm.perf_counter_ns()
        q_temp.append(q_end - q_start)
    merge_time.append(m_temp)
    counting_time.append(c_temp)
    quicksort_time.append(q_temp)

merge=Results(merge_time)
counting=Results(counting_time)
quick=Results(quicksort_time)

plt.figure(1)
plt.plot(sizes,merge.means,label="Merge sort mean")
plt.plot(sizes,counting.means,label="Counting sort mean")
plt.plot(sizes,quick.means,label="Quicksort mean")
plt.title("Mean sorting time for sorting algorithms")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(sizes,merge.mins,label="mins",s=10)
plt.scatter(sizes,merge.maxs,label="maxs",s=10)
plt.scatter(sizes,merge.means,label="means",s=10)
plt.title("Merge sort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(sizes,counting.mins,label="mins",s=10)
plt.scatter(sizes,counting.maxs,label="maxs",s=10)
plt.scatter(sizes,counting.means,label="means",s=10)
plt.title("Counting sort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(sizes,quick.mins,label="mins",s=10)
plt.scatter(sizes,quick.maxs,label="maxs",s=10)
plt.scatter(sizes,quick.means,label="means",s=10)
plt.title("Quicksort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.show()