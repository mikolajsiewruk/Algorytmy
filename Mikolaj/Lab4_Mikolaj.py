import random
import time as tm
import matplotlib.pyplot as plt

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
class Sorter:
    def __init__(self):
        self.merge_sorted=[]
        self.counting_sorted=[]
        self.quicksorted=[]
    def merge_sort(self,arr):
        if len(arr) > 1:
            mid = int(len(arr) // 2)
            L = arr[:mid]
            R = arr[mid:]
            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def counting_sort(self,arr):
        top = max(arr)
        new = []
        zeros = [0] * (top + 1)
        for i in range(len(arr)):
            zeros[arr[i]] = zeros[arr[i]] + 1
        for j in range(len(zeros)):
            if zeros[j] != 0:
                new.append(j)
        return new

    def quicksort(self,arr):
        if len(arr) >= 2:
            pivot = arr[-2]
            l = 0
            r = len(arr) - 1
            while l < r:
                if arr[l] > pivot and arr[r] < pivot:
                    arr[l], arr[r] = arr[r], arr[l]
                elif arr[l] == pivot and arr[r] < pivot:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                elif arr[r] == pivot and arr[l] > pivot:
                    arr[l], arr[r] = arr[r], arr[l]
                    r -= 1
                elif arr[l] >= pivot:
                    r -= 1
                elif arr[r] <= pivot:
                    l += 1
                else:
                    l += 1
                    r -= 1
            c = arr.count(pivot)
            left = arr[:arr.index(pivot) + c]
            right = arr[arr.index(pivot) + c:]
            if not left or not right:
                arr = left + right
                return arr
            a = self.quicksort(left)
            b = self.quicksort(right)
            arr = a + b
        return arr
def generate_vector():
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
sorter=Sorter()

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
