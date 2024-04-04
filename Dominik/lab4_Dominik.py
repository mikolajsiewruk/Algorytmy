import random as rnd
import time as tm
import copy
import matplotlib.pyplot as plt

# Początkowa wersja merge_sort rozdzielona na 3 funkcje xD
# def split(to_split):
#     if len(to_split) <=1:
#         return to_split
#     else:
#         mid=int(len(to_split) / 2)
#         a1= to_split[0:mid]
#         a2= to_split[mid:]
#         return split(a1) + split(a2)
#
# def merge(left, right):
#     merged = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i+=1
#         else:
#             merged.append(right[j])
#             j+=1
#
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged
#
# def merge_sort(to_sort):
#     if len(to_sort) <= 1:
#         return to_sort
#     splited = split(to_sort)
#     return merge(merge_sort(splited[:len(splited)//2]), merge_sort(splited[len(splited)//2:]))

def merge_sort(to_sort):
    if len(to_sort) <= 1:
        return to_sort

    mid = len(to_sort) // 2
    left = merge_sort(to_sort[:mid])
    right = merge_sort(to_sort[mid:])

    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def count_sort(to_sort):
    min_ = min(to_sort)
    max_ = max(to_sort)
    list_ = [0] * (max_ - min_ + 1)
    for i in range(len(to_sort)):
        list_[to_sort[i] - min_] += 1
    sorted = []
    for i in range(len(list_)):
        for j in range(0, list_[i]):
            sorted.append(i + min_)
    return sorted


def quick_sort(to_sort):
    if len(to_sort) <= 1:
        return to_sort
    pivot = to_sort[len(to_sort)//2]
    left = [x for x in to_sort if x < pivot]
    middle = [x for x in to_sort if x == pivot]
    right = [x for x in to_sort if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def arrays_creation(N, vector_sizes):
    #N is a number of repetitions, vector_sizes is a vector of sizes of vectors to be sorted
    x = []
    for i in range(len(vector_sizes)):
        x.append([])
        for j in range(N):
            x[i].append([])
    m_a = copy.deepcopy(x)
    c_a = copy.deepcopy(x)
    q_a = copy.deepcopy(x)
    m_t = copy.deepcopy(x)
    c_t = copy.deepcopy(x)
    q_t = copy.deepcopy(x)

    return m_a, c_a, q_a, m_t, c_t, q_t


def values_of_sorting(vector_sizes, sorting_times):
    minimum = []
    maximum = []
    mean = []
    for i in range(len(vector_sizes)):
        minimum.append(min(sorting_times[i]))
        maximum.append(max(sorting_times[i]))
        mean.append(sum(sorting_times[i])/len(sorting_times[i]))
    return minimum, maximum, mean


def sorting(N, vector_sizes):
    m_arrays, c_arrays, q_arrays, m_times, c_times, q_times = arrays_creation(N, vector_sizes)
    for i in range(N):
        for j in range(len(vector_sizes)):
            wektor = [rnd.randint(0,500) for _ in range(vector_sizes[j])]
            m_arrays[j][i] = wektor.copy()
            c_arrays[j][i] = wektor.copy()
            q_arrays[j][i] = wektor.copy()
    for i in range(N):
        for j in range(len(vector_sizes)):
            start = tm.perf_counter_ns()
            merge_sort(m_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            m_times[j][i] = czas

            start = tm.perf_counter_ns()
            count_sort(c_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            c_times[j][i] = czas

            start = tm.perf_counter_ns()
            quick_sort(q_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            # print(quick_sort(q_arrays[j][i]))
            q_times[j][i] = czas
    m_min, m_max, m_mean = values_of_sorting(vector_sizes, m_times)
    c_min, c_max, c_mean = values_of_sorting(vector_sizes, c_times)
    q_min, q_max, q_mean = values_of_sorting(vector_sizes, q_times)

    plt.figure(1)
    plt.plot(vector_sizes, m_mean, label = "Merge sort")
    plt.plot(vector_sizes, c_mean, label="Count sort")
    plt.plot(vector_sizes, q_mean, label="Quick sort")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Średni czas sortowania [ns]")
    plt.title("Zależność średniego czasu sortowania od długości wektora")
    plt.legend()
    plt.grid(True)

    plt.figure(2)
    plt.plot(vector_sizes, m_mean, label="Średni czas")
    plt.plot(vector_sizes, m_min, label="Minimalny czas")
    plt.plot(vector_sizes, m_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas Merge sort")
    plt.legend()
    plt.grid(True)

    plt.figure(3)
    plt.plot(vector_sizes, c_mean, label="Średni czas")
    plt.plot(vector_sizes, c_min, label="Minimalny czas")
    plt.plot(vector_sizes, c_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas Count sort")
    plt.legend()
    plt.grid(True)

    plt.figure(4)
    plt.plot(vector_sizes, q_mean, label="Średni czas")
    plt.plot(vector_sizes, q_min, label="Minimalny czas")
    plt.plot(vector_sizes, q_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas Quick sort")
    plt.legend()
    plt.grid(True)

    plt.show()

    return 0


sizes = [50, 100, 200, 500, 1000, 2000]
x = input("Podaj liczbę iteracji programu:")
if x.isdigit():
    x = int(x)
    if x > 0:
        sorting(x, sizes)
    else:
        print("Liczba iteracji musi być większa od 0")
else:
    print("Liczba iteracji musi byc liczbą")