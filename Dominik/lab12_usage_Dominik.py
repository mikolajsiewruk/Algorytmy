from Dominik.lab12_Dominik import Graph
import time as tm
import random as rnd
import numpy as np
import matplotlib.pyplot as plt

sizes = [5, 10, 15, 20]
results_dijkstra = [[], [], [], []]
results_kruskal = [[], [], [], []]
results_prim = [[], [], [], []]
for i in range(len(sizes)):
    for j in range(100):

        g = Graph()
        matrix = g.generate_random_graph(sizes[i])


        start = tm.perf_counter_ns()
        g.dijkstra(matrix, rnd.randint(1, len(matrix)-1), rnd.randint(1, len(g.matrix) - 1))
        results_dijkstra[i].append(tm.perf_counter_ns()-start)

        start = tm.perf_counter_ns()
        g.Kruskal(matrix, [rnd.randint(1, len(g.matrix) - 1) for _ in range(sizes[i])])
        results_kruskal[i].append(tm.perf_counter_ns() - start)

        start = tm.perf_counter_ns()
        g.Prim(matrix, [rnd.randint(1, len(g.matrix) - 1) for _ in range(sizes[i])])
        results_prim[i].append(tm.perf_counter_ns() - start)

dijkstra_mean = []
kruskal_mean = []
prim_mean = []
for i in range(len(results_dijkstra)):
    dijkstra_mean.append(np.mean(results_dijkstra[i]))
    kruskal_mean.append(np.mean(results_kruskal[i]))
    prim_mean.append(np.mean(results_prim[i]))

plt.plot(sizes, dijkstra_mean, label='Dijkstra')
plt.plot(sizes, kruskal_mean, label='Kruskal')
plt.plot(sizes, prim_mean, label='Prim')
plt.legend()
plt.show()