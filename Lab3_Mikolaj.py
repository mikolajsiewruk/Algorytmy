from random import randint
import time as tm
import matplotlib.pyplot as plt

class Results:
    def __init__(self):
        self.time50=[]
        self.time100=[]
        self.time200=[]
        self.time500=[]
        self.time1000=[]
        self.time2000=[]

class R1(Results):
    def __init__(self,time_arr):
        super().__init__()
        self.time_arr=time_arr
        self.mins=[]
        self.maxs=[]
        self.means=[]
        self.separate_arrays()
        self.get_stats()
    def separate_arrays(self):
        for i in range(0,len(self.time_arr)):
            self.time50.append(self.time_arr[i][0])
            self.time100.append(self.time_arr[i][1])
            self.time200.append(self.time_arr[i][2])
            self.time500.append(self.time_arr[i][3])
            self.time1000.append(self.time_arr[i][4])
            self.time2000.append(self.time_arr[i][5])
        print(self.time100)
    def get_stats(self):
        args=[self.time50,self.time100,self.time200,self.time500,self.time1000,self.time2000]
        for arr in args:
            self.mins.append(min(arr))
            self.maxs.append(max(arr))
            self.means.append(sum(arr)/len(arr))
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



bubble_time = []
insert_time = []
selection_time = []
sizes = [50, 100, 200, 500, 1000, 2000]

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

'''bubble_time = [bubble_sort(bubble_arrays[i])[0] for i in range(0, 6)]
insert_time = [insertion_sort(insert_arrays[i])[0] for i in range(0, 6)]
selection_time = [selection_sort(selection_arrays[i])[0] for i in range(0, 6)]'''


for i in range(0,10):
    bubble_arrays,insertion_arrays,selection_arrays=generate_vector()
    bubble_time.append([bubble_sort(bubble_arrays[i])[0] for i in range(0, 6)])
    insert_time.append([insertion_sort(insertion_arrays[i])[0] for i in range(0, 6)])
    selection_time.append([selection_sort(selection_arrays[i])[0] for i in range(0, 6)])
bubble=R1(bubble_time)
insertion=R1(insert_time)
selection=R1(selection_time)

fig,axs=plt.subplots(2)
axs[0].plot(sizes,bubble.means,label="Bubble sort means")
axs[0].plot(sizes,insertion.means,label="Insertion sort mean")
axs[0].plot(sizes,selection.means,label="Selection sort mean")

axs[0].legend()
axs[0].grid(True)
plt.show()
'''plt.plot(sizes, bubble_time, label="Bubble sort")
plt.plot(sizes, insert_time, label='Insertion sort')
plt.plot(sizes, selection_time, label='Selection sort')
plt.xlabel('Vector size')
plt.ylabel('Sorting time [ns]')
plt.title('Runtime Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()'''
