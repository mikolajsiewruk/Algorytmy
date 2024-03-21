import random as rnd
import time as tm
import copy
import matplotlib.pyplot as plt


def bubble_sort(to_sort):
    start = tm.perf_counter_ns()
    a = 1
    while a != 0:
        a = 0
        for i in range(len(to_sort) - 1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i + 1] = to_sort[i + 1], to_sort[i]
                a+=1
    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas, to_sort


def insertion_sort(to_sort):
    start = tm.perf_counter_ns()
    for i in range(1, len(to_sort)):
        check = to_sort[i]
        ind_sorted = i-1

        while ind_sorted>=0 and check < to_sort[ind_sorted]:
            to_sort[ind_sorted + 1] = to_sort[ind_sorted]
            ind_sorted -= 1

        to_sort[ind_sorted + 1] = check

    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas, to_sort


def selection_sort(to_sort):
    start = tm.perf_counter_ns()
    for i in range(len(to_sort)):
        ind = i
        for j in range(i + 1, len(to_sort)):
            if to_sort[j] < to_sort[ind]:
                ind = j
        to_sort[i], to_sort[ind] = to_sort[ind], to_sort[i]

    stop = tm.perf_counter_ns()
    czas = stop - start
    return czas, to_sort


def arrays_creation(N, vector_sizes):
    #N is a number of repetitions, vector_sizes is a vector of sizes of vectors to be sorted
    x = []
    for i in range(len(vector_sizes)):
        x.append([])
        for j in range(N):
            x[i].append([])
    b_a = copy.deepcopy(x)
    i_a = copy.deepcopy(x)
    s_a = copy.deepcopy(x)
    b_t = copy.deepcopy(x)
    i_t = copy.deepcopy(x)
    s_t = copy.deepcopy(x)

    return b_a, i_a, s_a, b_t, i_t, s_t


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
    b_arrays, i_arrays, s_arrays, b_times, i_times, s_times = arrays_creation(N, vector_sizes)
    for i in range(N):
        for j in range(len(vector_sizes)):
            wektor = [rnd.randint(0,500) for _ in range(vector_sizes[j])]
            b_arrays[j][i] = wektor.copy()
            i_arrays[j][i] = wektor.copy()
            s_arrays[j][i] = wektor.copy()
    for i in range(N):
        for j in range(len(vector_sizes)):
            b_times[j][i] = bubble_sort(b_arrays[j][i])[0]
            i_times[j][i] = insertion_sort(i_arrays[j][i])[0]
            s_times[j][i] = selection_sort(s_arrays[j][i])[0]
    b_min, b_max, b_mean = values_of_sorting(vector_sizes, b_times)
    i_min, i_max, i_mean = values_of_sorting(vector_sizes, i_times)
    s_min, s_max, s_mean = values_of_sorting(vector_sizes, s_times)

    plt.figure(1)
    plt.plot(vector_sizes, b_mean, label = "Bubble sort")
    plt.plot(vector_sizes, i_mean, label="Insertion sort")
    plt.plot(vector_sizes, s_mean, label="Selection sort")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Średni czas sortowania [ns]")
    plt.title("Zależność średniego czasu sortowania od długości wektora")
    plt.legend()
    plt.grid(True)

    plt.figure(2)
    plt.plot(vector_sizes, b_mean, label="Średni czas")
    plt.plot(vector_sizes, b_min, label="Minimalny czas")
    plt.plot(vector_sizes, b_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas bubble sort")
    plt.legend()
    plt.grid(True)

    plt.figure(3)
    plt.plot(vector_sizes, i_mean, label="Średni czas")
    plt.plot(vector_sizes, i_min, label="Minimalny czas")
    plt.plot(vector_sizes, i_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas insertion sort")
    plt.legend()
    plt.grid(True)

    plt.figure(4)
    plt.plot(vector_sizes, s_mean, label="Średni czas")
    plt.plot(vector_sizes, s_min, label="Minimalny czas")
    plt.plot(vector_sizes, s_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas selection sort")
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