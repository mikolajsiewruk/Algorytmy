from random import randint
import time as tm
import matplotlib.pyplot as plt


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


bubble_arrays = []
insert_arrays = []
selection_arrays = []
bubble_time = []
insert_time = []
selection_time = []
sizes = [50, 100, 200, 500, 1000, 2000]

for i in range(0, len(sizes)):
    a = [randint(0, 5000) for _ in range(0, sizes[i])]
    bubble_arrays.append(a.copy())
    insert_arrays.append(a.copy())
    selection_arrays.append(a.copy())

bubble_time = [bubble_sort(bubble_arrays[i])[0] for i in range(0, 6)]
insert_time = [insertion_sort(insert_arrays[i])[0] for i in range(0, 6)]
selection_time = [selection_sort(selection_arrays[i])[0] for i in range(0, 6)]

plt.plot(sizes, bubble_time, label="Bubble sort")
plt.plot(sizes, insert_time, label='Insertion sort')
plt.plot(sizes, selection_time, label='Selection sort')
plt.xlabel('Vector size')
plt.ylabel('Sorting time [ns]')
plt.title('Runtime Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
