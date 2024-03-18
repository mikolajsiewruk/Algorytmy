import random as rnd
import time as tm
import matplotlib.pyplot as plt

def bubble_sort(sort):
    start = tm.perf_counter_ns()
    a = 1
    while a != 0:
        a = 0
        for i in range(len(sort)-1):
            if sort[i] > sort[i+1]:
                sort[i], sort[i+1] = sort[i+1], sort[i]
                a+=1
    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas

def insertion_sort(sort):
    start = tm.perf_counter_ns()
    for i in range(1, len(sort)):
        check = sort[i]
        ind_sorted = i-1

        while ind_sorted>=0 and check < sort[ind_sorted]:
            sort[ind_sorted + 1] = sort[ind_sorted]
            ind_sorted -= 1

        sort[ind_sorted + 1] = check

    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas

def selection_sort(sort):
    start = tm.perf_counter_ns()
    for i in range(len(sort)):
        ind = i
        for j in range(i + 1, len(sort)):
            if sort[j] < sort[ind]:
                ind = j
        sort[i], sort[ind] = sort[ind], sort[i]

    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas

sizes = [50, 100, 200, 500, 1000, 2000]
def sorting(N):
    for i in range(N):
        for j in range(len(sizes)):
            wektor = [rnd.randint(0,500) for _ in range(sizes[j])]

    return wektor


print(sorting(10))