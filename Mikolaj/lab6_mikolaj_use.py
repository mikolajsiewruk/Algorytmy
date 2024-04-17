from Lab6_Mikolaj import BST, AVL
from Lab3_Mikolaj import Results
import numpy as np
import random
import time as tm
import matplotlib.pyplot as plt


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

        values = []
        time_bst_temp = 0
        time_avl_temp = 0

        for j in range(100): # mega ważne!!!! jeśli tutaj da się 100 tak jak jest w instrukcji, wykres avl wygląda jakby nie miał sensu, jednakże ma on właśnie wielki sens tylko trzeba to umieć uzasadnić
            values.append(random.randint(1, sizes[i]))

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

plt.plot(sizes,stats_avl.means, label = "AVL O(log(n))")
plt.plot(sizes,stats_bst.means, label = "BST O(n)")
plt.title("BST and AVL trees search time comparison")
plt.xlabel("Array size")
plt.ylabel("Search time")
plt.grid()
plt.legend()
plt.show()
