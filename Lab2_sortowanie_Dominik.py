import random as rnd
import time as tm

def random_array(minimum, maximum, size):
    ciag = []
    for i in range(size):
        ciag.append(rnd.randint(minimum, maximum))
    return ciag

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

# Niedziałające selection sort; metoda min nie sprawdza się przy powtarzających się wartościach
# Zostawiam dla potomnych, bo podoba mi się jak to napisałem xd

# def selection_sort(sort):
#     for i in range(len(sort)):
#         ind = sort.index(min(sort[i:]))
#         sort[i], sort[ind] = sort[ind], sort[i]
#     return sort

ciag_50 = random_array(0, 5000, 50)
ciag1_50 = ciag_50.copy()
ciag2_50 = ciag_50.copy()
ciag3_50 = ciag_50.copy()

ciag_100 = random_array(0, 5000, 100)
ciag1_100 = ciag_100.copy()
ciag2_100 = ciag_100.copy()
ciag3_100 = ciag_100.copy()

ciag_200 = random_array(0, 5000, 200)
ciag1_200 = ciag_200.copy()
ciag2_200 = ciag_200.copy()
ciag3_200 = ciag_200.copy()

ciag_500 = random_array(0, 5000, 500)
ciag1_500 = ciag_500.copy()
ciag2_500 = ciag_500.copy()
ciag3_500 = ciag_500.copy()

ciag_1000 = random_array(0, 5000, 1000)
ciag1_1000 = ciag_1000.copy()
ciag2_1000 = ciag_1000.copy()
ciag3_1000 = ciag_1000.copy()

ciag_2000 = random_array(0, 5000, 2000)
ciag1_2000 = ciag_2000.copy()
ciag2_2000 = ciag_2000.copy()
ciag3_2000 = ciag_2000.copy()

czas50 = bubble_sort(ciag1_50)
czas100 = bubble_sort(ciag1_100)
czas200 = bubble_sort(ciag1_200)
czas500 = bubble_sort(ciag1_500)
czas1000 = bubble_sort(ciag1_1000)
czas2000 = bubble_sort(ciag1_2000)