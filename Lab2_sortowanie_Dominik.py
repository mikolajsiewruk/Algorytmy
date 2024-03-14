import random as rnd
import time as tm
import matplotlib.pyplot as plt

def random_array(minimum, maximum, size):
    ciag = []
    for i in range(size):
        ciag.append(rnd.randint(minimum, maximum))
    return ciag

def bubble_sort(o):
    start = tm.perf_counter_ns()
    a = 1
    while a != 0:
        a = 0
        for i in range(len(o) - 1):
            if o[i] > o[i + 1]:
                o[i], o[i + 1] = o[i + 1], o[i]
                a+=1
    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas

def insertion_sort(o):
    start = tm.perf_counter_ns()
    for i in range(1, len(o)):
        check = o[i]
        ind_sorted = i-1

        while ind_sorted>=0 and check < o[ind_sorted]:
            o[ind_sorted + 1] = o[ind_sorted]
            ind_sorted -= 1

        o[ind_sorted + 1] = check

    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas

def selection_sort(o):
    start = tm.perf_counter_ns()
    for i in range(len(o)):
        ind = i
        for j in range(i + 1, len(o)):
            if o[j] < o[ind]:
                ind = j
        o[i], o[ind] = o[ind], o[i]

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

sizes = [50, 100, 200, 500, 1000, 2000]
times_bubble = [bubble_sort(ciag1_50), bubble_sort(ciag1_100), bubble_sort(ciag1_200), bubble_sort(ciag1_500),
                bubble_sort(ciag1_1000), bubble_sort(ciag1_2000)]
times_insertion = [insertion_sort(ciag2_50), insertion_sort(ciag2_100), insertion_sort(ciag2_200),
                   insertion_sort(ciag2_500), insertion_sort(ciag2_1000), insertion_sort(ciag2_2000)]
times_selection = [selection_sort(ciag3_50), selection_sort(ciag3_100), selection_sort(ciag3_200),
                   selection_sort(ciag3_500), selection_sort(ciag3_1000), selection_sort(ciag3_2000)]

plt.plot(sizes, times_bubble, label = "Bubble sort")
plt.plot(sizes, times_insertion, label = 'Insertion sort')
plt.plot(sizes, times_selection, label = 'Selection sort')
plt.xlabel('Rozmiar wektora')
plt.ylabel('Czas sortowania [ns]')
plt.title('Porównanie sortowań i ich czasów')
plt.legend()
plt.grid(True)
plt.show()

# print(insertion_sort(ciag2_1000))
# print(selection_sort(ciag3_1000))