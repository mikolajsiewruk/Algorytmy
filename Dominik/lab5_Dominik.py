import random as rnd
import matplotlib.pyplot as plt
import time as tm
import copy

#  PUNKTY 1 i 2 instrukcji
class Node1:
    def __init__(self, value):
        self.value = value
        self.left = None
        self. right = None

    def insert_left_leaf(self, value):
        self.left = value

    def insert_right_leaf(self, value):
        self.right = value

    def insert_left_node(self, value):
        self.left = Node1(value)

    def insert_right_node(self, value):
        self.right = Node1(value)

    def get_value_left(self):
        if type (self.left) == int:
            return self.left
        else:
            return self.left.value

    def get_value_right(self):
        if type (self.right) == int:
            return self.right
        else:
            return self.right.value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()





wektor = []
for i in range(10):
    wektor.append(rnd.randint(1,10))

print(wektor)

abc = Node1(wektor[0])
abc.insert_left_node(wektor[1])
abc.insert_right_node(wektor[2])
abc.left.insert_left_node(wektor[3])
abc.left.insert_right_node(wektor[4])
abc.right.insert_left_node(wektor[5])
abc.right.insert_right_node(wektor[6])
abc.left.left.insert_left_node(wektor[7])
abc.left.left.insert_right_node(wektor[8])
abc.left.right.insert_left_node(wektor[9])
abc.print_tree()


# PUNKTY 3 i 4 INSTRUKCJI
class TreeNode:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Tree:

    def __init__(self,arr):
        self.arr=arr
        self.root=TreeNode(arr[0])

    def add_node(self,node,val):
        q=[] # kolejka nodów do sprawdzenia
        q.append(node)
        # metoda dodaje nody od lewej, jeśli chcemy od prawej to trzeba zamienić ify kolejnością
        while q:
            current=q[0] # sprawdzany node to 1. z kolejki
            q.pop(0)
            if not current.left: # sprawdza czy node ma lewą stronę
                print(f"{current.val}  added {val} left")
                current.left=TreeNode(val) # jesli nie to dodaj lewego nołda i zakończ sprawdzanie
                break
            else:
                q.append(current.left)
            if not current.right: # to samo co dla lewej strony
                print(f"{current.val}  added {val} right")
                current.right=TreeNode(val)
                break
            else:
                q.append(current.right)
    def make_tree(self):
        for i in range(1,len(self.arr)):
            self.add_node(self.root,self.arr[i])

    def print_tree(self,node):
        if not node:
            return
        self.print_tree(node.left)
        print(node.val, end=" ")
        self.print_tree(node.right)

class MaxHeap:
    def __init__(self,arr):
        self.graph=[]
        self.arr=arr
        self.root=TreeNode(max(self.arr))
        self.arr.remove(max(self.arr))
        self.temp=self.arr

    def add_node(self, node, val):
        q = []
        q.append(node)
        while q:
            current = q[0]
            q.pop(0)
            if not current.left:
                print(f"{current.val}  added {val} left")
                current.left = TreeNode(val)
                self.graph.append((f'{current.val}',f'{current.left.val}'))
                break
            else:
                q.append(current.left)
            if not current.right:
                print(f"{current.val}  added {val} right")
                current.right = TreeNode(val)
                self.graph.append((f'{current.val}',f'{current.right.val}'))
                break
            else:
                q.append(current.right)

    def make_heap(self):
        temp=self.temp
        for i in range(len(self.temp)):
            m=max(temp)
            self.add_node(self.root,m)
            temp.remove(m)
        return self.graph

h=MaxHeap(wektor)
print(h.make_heap())


def heapify(arr, N, i):  # N to wielkość tablicy, i to indeks elementu który sprawdzamy
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child = 2*i + 1
    r = 2 * i + 2  # right child = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # jeśli jakiś child jest większy od roota trzeba go zmienić
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, N, largest)


def heapsort(arr):
    N = len(arr)

    # Build a maxheap. od końca tablicy
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N - 1, 0, -1):  # od tyłu zamieniaj elementy
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

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
    h_a = copy.deepcopy(x)
    m_a = copy.deepcopy(x)
    c_a = copy.deepcopy(x)
    q_a = copy.deepcopy(x)
    h_t = copy.deepcopy(x)
    m_t = copy.deepcopy(x)
    c_t = copy.deepcopy(x)
    q_t = copy.deepcopy(x)

    return h_a, m_a, c_a, q_a, h_t, m_t, c_t, q_t


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
    h_arrays, m_arrays, c_arrays, q_arrays, h_times, m_times, c_times, q_times = arrays_creation(N, vector_sizes)
    for i in range(N):
        for j in range(len(vector_sizes)):
            wektor = [rnd.randint(0,500) for _ in range(vector_sizes[j])]
            h_arrays[j][i] = wektor.copy()
            m_arrays[j][i] = wektor.copy()
            c_arrays[j][i] = wektor.copy()
            q_arrays[j][i] = wektor.copy()
    for i in range(N):
        for j in range(len(vector_sizes)):

            start = tm.perf_counter_ns()
            x = heapsort(h_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            print(x)
            h_times[j][i] = czas

            start = tm.perf_counter_ns()
            x = merge_sort(m_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            # print(x)
            m_times[j][i] = czas

            start = tm.perf_counter_ns()
            x = count_sort(c_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            # print(x)
            c_times[j][i] = czas

            start = tm.perf_counter_ns()
            x = quick_sort(q_arrays[j][i])
            stop = tm.perf_counter_ns()
            czas = stop - start
            # print(x)
            q_times[j][i] = czas
    h_min, h_max, h_mean = values_of_sorting(vector_sizes, h_times)
    m_min, m_max, m_mean = values_of_sorting(vector_sizes, m_times)
    c_min, c_max, c_mean = values_of_sorting(vector_sizes, c_times)
    q_min, q_max, q_mean = values_of_sorting(vector_sizes, q_times)

    plt.figure(1)
    plt.plot(vector_sizes, h_mean, label = "Heap sort")
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

    plt.figure(5)
    plt.plot(vector_sizes, h_mean, label="Średni czas")
    plt.plot(vector_sizes, h_min, label="Minimalny czas")
    plt.plot(vector_sizes, h_max, label="Maksymalny czas")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas [ns]")
    plt.title("Minimalny, maksymalny i średni czas Heap sort")
    plt.legend()
    plt.grid(True)

    plt.show()

    return 0

sizes = [50, 100, 200, 500, 1000, 2000]
sorting(10, sizes)