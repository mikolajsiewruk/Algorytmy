import random as rnd
import time as tm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self, arr: list):
        self.arr = arr
        self.root = Node(self.arr[0])

# Wyszukiwanie największego elementu
    def maksimum(self, node):
        maksimum = node
        if node.right:
            maksimum = self.maksimum(node.right)
        return maksimum

# Wyszukiwanie najmniejszego elementu
    def minimum(self, node):
        minimum = node
        if node.left:
            minimum = self.minimum(node.left)
        return minimum

# Wyszukiwanie następnika
    def next(self, node):
        if node.right:
            return self.minimum(node.right)
        else:
            return None

# Wyszukiwanie poprzednika
    def previous(self, node):
        if node.left:
            return self.maksimum(node.left)
        else:
            return None


# Wyszukiwanie elementu
    def search(self, node, key, parent=None):
        if not node:
            return False
        else:
            if node.key == key:
                return node, parent
            elif key > node.key:
                return self.search(node.right, key, node)
            else:
                return self.search(node.left, key, node)


# Wstawianie elementu
    def insert(self, node, key):
        if node.key:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.insert(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.insert(node.right, key)
        else:
            node.key = key

# Usuwanie elementu
    def remove(self, key):
        node, parent = self.search(self.root, key)
        if node.key:
            # Brak dzieci
            if node.left is None and node.right is None:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
                del node
            # Tylko lewe dziecko
            elif node.left and not node.right:
                if parent:
                    if parent.left is node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    self.root = node.left
                del node
            # Tylko prawe dziecko
            elif node.right and not node.left:
                if parent:
                    if parent.right is node:
                        parent.right = node.right
                    else:
                        parent.left = node.right
                else:
                    self.root = node.right
                del node
            # Dwoje dzieci
            else:
                successor = self.next(node)
                node.key = successor.key
                successor_parent = self.search(node.right, successor.key)[1]
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                del successor

class AVL(BST):

    def check_balance(self, node):
        if node == None:
            return 0
        else:
            return max(self.check_balance(node.left), self.check_balance(node.right)) + 1

    def rotate_right(self, node):
        R = node.left
        node.left = R.right
        R.right = node
        node = R

    def rotate_left(self, node):
        L = node.right
        node.right = L.left
        L.left = node
        node = L

    def balance(self, node):
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        while balance_factor not in [-1, 0, 1]:
            # print(balance_factor)
            if balance_factor > 1:
                # print('left lacking')
                self.rotate_right(node)
            else:
                # print('right')
                self.rotate_left(node)
            balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
            # print(node.value)

    def insert(self, node, key):  # fix to check every node for balance
        if node.key:
            if key > node.key:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.insert(node.right, key)
            else:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.insert(node.left, key)
        balance_factor = self.check_balance(node.left) - self.check_balance(node.right)
        if balance_factor not in [-1, 0, 1]:
            self.balance(node)

    def remove(self, key):
        node, parent = self.search(self.root, key)
        if node.key:
            # Brak dzieci
            if node.left is None and node.right is None:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
                del node
            # Tylko lewe dziecko
            elif node.left and not node.right:
                if parent:
                    if parent.left is node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    self.root = node.left
                del node
            # Tylko prawe dziecko
            elif node.right and not node.left:
                if parent:
                    if parent.right is node:
                        parent.right = node.right
                    else:
                        parent.left = node.right
                else:
                    self.root = node.right
                del node
            # Dwoje dzieci
            else:
                successor = self.next(node)
                node.key = successor.key
                successor_parent = self.search(node.right, successor.key)[1]
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                del successor
        balance_factor = self.check_balance(self.root.left) - self.check_balance(self.root.right)
        if balance_factor not in [-1, 0, 1]:
            self.balance(self.root)

# def arrays_creation(N, vector_sizes):
#     #N is a number of repetitions, vector_sizes is a vector of sizes of vectors to be sorted
#     x = []
#     for i in range(len(vector_sizes)):
#         x.append([])
#         for j in range(N):
#             x[i].append([])
#     bst_arrays = copy.deepcopy(x)
#     avl_arrays = copy.deepcopy(x)
#     return bst_arrays, avl_arrays
#
# def generate(N, vector_sizes):
#     bst_arrays, avl_arrays = arrays_creation(N, vector_sizes)
#     for i in range(N):
#         for j in range(len(vector_sizes)):
#             wector = []
#             while len(wector) < vector_sizes[j]:
#                 x = rnd.randint(1, vector_sizes[j])
#                 if x not in wector:
#                     wector.append(x)
#             bst_arrays[j][i] = wector.copy()
#             avl_arrays[j][i] = wector.copy()
#     return bst_arrays, avl_arrays
#
# def to_search():
#
#
# vector_sizes = [15, 50, 100, 500, 1000, 2000]
# print(generate(10, vector_sizes)[0])
class Results:
    def __init__(self, time_arr):
        super().__init__()
        self.time_arr = time_arr
        self.time50 = []
        self.time100 = []
        self.time200 = []
        self.time500 = []
        self.time1000 = []
        self.time2000 = []
        self.mins = []
        self.maxs = []
        self.means = []
        self.separate_arrays()
        self.get_stats()

    def separate_arrays(self):
        for i in range(0, len(self.time_arr)):
            self.time50.append(self.time_arr[i][0])
            self.time100.append(self.time_arr[i][1])
            self.time200.append(self.time_arr[i][2])
            self.time500.append(self.time_arr[i][3])
            self.time1000.append(self.time_arr[i][4])
            self.time2000.append(self.time_arr[i][5])

    # metoda licząca statystyki w każdej z wydzielonych wcześniej tabel
    def get_stats(self):
        args = [self.time50, self.time100, self.time200, self.time500, self.time1000, self.time2000]

        # pętla dla każdej z tabel liczy jej statystyki i dodaje do tabeli statycstycznych
        for arr in args:
            self.mins.append(min(arr))
            self.maxs.append(max(arr))
            self.means.append(sum(arr) / len(arr))

def generate():
    sizes = [50, 100, 200, 500, 1000, 2000]  # not the best design
    bst_arrays = []
    avl_arrays = []
    arr = []
    for j in range(len(sizes)):
        for i in range(1, sizes[j]+1):
            arr.append(i)
        np.random.shuffle(arr)
        temp = arr.copy()
        bst_arrays.append(temp)
        avl_arrays.append(temp)
    return bst_arrays, avl_arrays


sizes = [50, 100, 200, 500, 1000, 2000]
time_bst = []
time_avl = []

for k in range(100):
    arr = generate()
    t_bst = []
    t_avl = []
    for i in range(len(sizes)):
        bst = BST(arr[0][i])
        avl = AVL(arr[1][i])
        print(avl.check_balance(avl.root.right),avl.check_balance(avl.root.left))

        values = []
        time_bst_temp = 0
        time_avl_temp = 0

        for j in range(100): # mega ważne!!!! jeśli tutaj da się 100 tak jak jest w instrukcji, wykres avl wygląda jakby nie miał sensu, jednakże ma on właśnie wielki sens tylko trzeba to umieć uzasadnić
            values.append(rnd.randint(1, sizes[i]))

        for val in values:
            t1 = tm.perf_counter_ns()
            bst.search(bst.root,val)
            t2 = tm.perf_counter_ns()
            time_bst_temp += t2-t1

            t3 = tm.perf_counter_ns()
            avl.search(avl.root,val)
            t4 = tm.perf_counter_ns()
            time_avl_temp += t4-t3

        t_bst.append(time_bst_temp)
        t_avl.append(time_avl_temp)
    time_bst.append(t_bst)
    time_avl.append(t_avl)

stats_avl = Results(time_avl)
stats_bst = Results(time_bst)
print(stats_avl.means,stats_bst.means )

plt.plot(sizes,stats_avl.means, label = "AVL")
plt.plot(sizes,stats_bst.means, label = "BST")
plt.title("BST and AVL trees search time comparison")
plt.xlabel("Array size")
plt.ylabel("Search time")
plt.grid()
plt.legend()
plt.show()
# data = {
#     "BST" : [czas_BST15],
#     "AVL" : [czas_AVL15]
# }
#
# df = pd.DataFrame(data, index = ["5 z 15"])
# print(df)