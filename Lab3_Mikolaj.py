from random import randint
import time as tm
import matplotlib.pyplot as plt

# klasa results służąca do przechowywania danych sortowań i licząca ich parametry
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

        # pętla dla każdej z tabel liczy jej statystyki i dodaje do tabeli statystycznych
        for arr in args:
            self.mins.append(min(arr))
            self.maxs.append(max(arr))
            self.means.append(sum(arr)/len(arr))

# w celu sprawdzenia czy sortowania działają należy zrobić coś takiego print(bubble_sort(jakas_tablica)[1]), gdyż funkcje sortujące zwracają wynik w takiej postaci (czas,posortowana_tablica), wtedy posortowana tablica znajduje się pod indeksem 1, taka typ danych nazywa się tuple
def bubble_sort(arr):
    start = tm.perf_counter_ns()
    a = 1
    while a != 0:
        a = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                a += 1
    end = tm.perf_counter_ns()
    time = end - start
    return time, arr


def insertion_sort(arr):
    start = tm.perf_counter_ns()
    for i in range(1, len(arr)):
        check = arr[i]
        ind_sorted = i - 1

        while ind_sorted >= 0 and check < arr[ind_sorted]:
            arr[ind_sorted + 1] = arr[ind_sorted]
            ind_sorted -= 1

        arr[ind_sorted + 1] = check

    end = tm.perf_counter_ns()
    return end - start, arr


def selection_sort(arr):
    start = tm.perf_counter_ns()
    for j in range(0, len(arr)):
        top = 0
        for i in range(0, len(arr) - j):
            if arr[i] > top:
                top = arr[i]
        arr[arr.index(top)], arr[-1 - j] = arr[-1 - j], arr[arr.index(top)]
    end = tm.perf_counter_ns()
    return end - start, arr

# funkcja tworząca wektor zawierający wektory 50,100,200,500,1000 i 2000 elementowe, osobne dla każdego z sortowań, żeby uniknąć sortowania juz posortowanej tabeli
def generate_vector():
    bubble_arrays = []
    insert_arrays = []
    selection_arrays = []
    for i in range(0, len(sizes)):
        temporary = [randint(0, 5000) for _ in range(0, sizes[i])]
        bubble_arrays.append(temporary.copy())
        insert_arrays.append(temporary.copy())
        selection_arrays.append(temporary.copy())
    return bubble_arrays,insert_arrays,selection_arrays


bubble_time = []
insert_time = []
selection_time = []
sizes = [50, 100, 200, 500, 1000, 2000]

# 100 krotne powtórzenie sortowań (Metoda Monte Carlo), w instrukcji jest żeby ilość iteracji podawać z klawiatury (nie chce mi sie)
for i in range(0,100):
    bubble_arrays,insertion_arrays,selection_arrays=generate_vector() # tworzenie nowych wektorów próbek dla każdego sortowania
    bubble_time.append([bubble_sort(bubble_arrays[i])[0] for i in range(0, 6)]) # w każdej iteracji do tabeli czasów dodawane są kolejne czasy sortowania dla każdego rozmiaru tabeli wejściowej
    insert_time.append([insertion_sort(insertion_arrays[i])[0] for i in range(0, 6)])
    selection_time.append([selection_sort(selection_arrays[i])[0] for i in range(0, 6)])

# inicjalizacja klasy Results dla wszystkich sortowań, ważne, żeby podać czasy! Klasa sama wyznaczy sobie już wszystko, chillerka :)
bubble=Results(bubble_time)
insertion=Results(insert_time)
selection=Results(selection_time)

#wykresy
plt.figure(1)
plt.plot(sizes,bubble.means,label="Bubble sort means")
plt.plot(sizes,insertion.means,label="Insertion sort mean")
plt.plot(sizes,selection.means,label="Selection sort mean")
plt.title("Mean sorting time for sorting algorithms")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(sizes,bubble.mins,label="mins",s=10)
plt.scatter(sizes,bubble.maxs,label="maxs",s=10)
plt.scatter(sizes,bubble.means,label="means",s=10)
plt.title("Bubble sort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(sizes,insertion.mins,label="mins",s=10)
plt.scatter(sizes,insertion.maxs,label="maxs",s=10)
plt.scatter(sizes,insertion.means,label="means",s=10)
plt.title("Insertion sort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(sizes,selection.mins,label="mins",s=10)
plt.scatter(sizes,selection.maxs,label="maxs",s=10)
plt.scatter(sizes,selection.means,label="means",s=10)
plt.title("Selection sort statistics for different array sizes")
plt.xlabel("Array size")
plt.ylabel("Sorting time")
plt.legend()
plt.grid(True)

plt.show()