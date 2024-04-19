import random as rnd
import time as tm
import copy
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
            potential = None
            current = self.root
            while current is not node:
                if node.key < current.key:
                    potential = current
                    current = current.left
                else:
                    current = current.right
            return potential


# Wyszukiwanie poprzednika
    def previous(self, node):
        if node.left:
            return self.maksimum(node.left)
        else:
            potential = None
            current = self.root
            while current != node:
                if node.key > current.key:
                    potential = current
                    current = current.right
                else:
                    current = current.left
            return potential


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

wector_15 = []
while len(wector_15) < 15:
    x = rnd.randint(1, 15)
    if x not in wector_15:
        wector_15.append(x)

BST_15 = BST(wector_15)
AVL_15 = AVL(wector_15)
for el in wector_15[1:]:
    BST_15.insert(BST_15.root, el)
    AVL_15.insert(AVL_15.root, el)

to_search = []
while len(to_search) <5:
    x = rnd.randint(1, 15)
    if x not in to_search:
        to_search.append(x)

czas_BST15 = 0
czas_AVL15 = 0
for el in to_search:
    start = tm.perf_counter_ns()
    BST_15.search(BST_15.root, el)
    stop = tm.perf_counter_ns()
    czas_BST15 = czas_BST15 + (stop - start)
    start = tm.perf_counter_ns()
    BST_15.search(BST_15.root, el)
    stop = tm.perf_counter_ns()
    czas_AVL15 = czas_AVL15 + (stop - start)


def arrays_creation(N, vector_sizes):
    #N is a number of repetitions, vector_sizes is a vector of sizes of vectors to be sorted
    x = []
    for i in range(len(vector_sizes)):
        x.append([])
        for j in range(N):
            x[i].append([])
    bst_arrays = copy.deepcopy(x)
    avl_arrays = copy.deepcopy(x)
    return bst_arrays, avl_arrays


def generate(N, vector_sizes):
    bst_arrays, avl_arrays = arrays_creation(N, vector_sizes)
    for i in range(N):
        for j in range(len(vector_sizes)):
            wector = []
            while len(wector) < vector_sizes[j]:
                x = rnd.randint(1, vector_sizes[j])
                if x not in wector:
                    wector.append(x)
            bst_arrays[j][i] = wector.copy()
            avl_arrays[j][i] = wector.copy()
    return bst_arrays, avl_arrays

def to_search(N, vector_sizes):
    bst_search, avl_search = arrays_creation(N, vector_sizes)
    for i in range(N):
        for j in range(len(vector_sizes)):
            wector = []
            if vector_sizes[j] == 50:
                while len(wector) < 100:
                    x = rnd.randint(1, vector_sizes[j])
                    wector.append(x)
            else:
                while len(wector) < 100:
                    x = rnd.randint(1, vector_sizes[j])
                    if x not in wector:
                        wector.append(x)
            bst_search[j][i] = wector.copy()
            avl_search[j][i] = wector.copy()
            wector.clear()
    return bst_search, avl_search

def statistics(N, vector_sizes):
    bst_arrays, avl_arrays = generate(N, vector_sizes)
    bst_search, avl_search = to_search(N, vector_sizes)
    times_bst = []
    times_avl = []
    for i in range(len(vector_sizes)):
        czas_bst = 0
        czas_avl = 0
        for j in range(N):
            bst = BST(bst_arrays[i][j])
            for el in bst_arrays[i][j][1:]:
                bst.insert(bst.root, el)

            for el in bst_search[i][j]:
                start = tm.perf_counter_ns()
                bst.search(bst.root, el)
                stop = tm.perf_counter_ns()
                czas_bst = czas_bst + (stop - start)

            del bst

            avl = AVL(avl_arrays[i][j])
            for el in avl_arrays[i][j][1:]:
                avl.insert(avl.root, el)

            for el in avl_search[i][j]:
                start = tm.perf_counter_ns()
                avl.search(avl.root, el)
                stop = tm.perf_counter_ns()
                czas_avl = czas_avl + (stop - start)

            del avl

        times_bst.append(czas_bst/N)
        times_avl.append(czas_avl/N)
    return times_bst, times_avl


vector_sizes = [50, 100, 500, 1000, 2000]
times_bst, times_avl = statistics(100, vector_sizes)


data = {
    "BST" : [czas_BST15, times_bst[0], times_bst[1], times_bst[2], times_bst[3], times_bst[4]],
    "AVL" : [czas_AVL15, times_avl[0], times_avl[1], times_avl[2], times_avl[3], times_avl[4]]
}

df = pd.DataFrame(data, index = ["5 z 15", "100 z 50", "100 ze 100", "100 z 500", "100 z 1000", "100 z 2000"])
print(df)

plt.plot(vector_sizes, times_avl, label = "AVL")
plt.plot(vector_sizes, times_bst, label = "BST")
plt.title("BST and AVL trees search time comparison")
plt.xlabel("Array size")
plt.ylabel("Search time")
plt.grid()
plt.legend()
plt.show()