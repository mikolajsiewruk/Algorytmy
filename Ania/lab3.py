from random import randint
import time as tm
import matplotlib.pyplot as plt

# klasa  do przechowywania danych sortowań i licząca ich parametry
class Wyniki:
    def __init__(self, czas_wektory):
        super().__init__()
        self.czas_wektory=czas_wektory
        self.czas_50 = []
        self.czas_100 = []
        self.czas_200 = []
        self.czas_500 = []
        self.czas_1000 = []
        self.czas_2000 = []
        self.mins=[]
        self.maxs=[]
        self.means=[]
        self.oddzielne_wektory()
        self.stat_sort()

    # metoda do wydobycia danych o czasie sortowania wektora o określonym rozmiarze
    def oddzielne_wektory(self):
        for i in range(0,len(self.czas_wektory)):
            self.czas_50.append(self.czas_wektory[i][0])
            self.czas_100.append(self.czas_wektory[i][1])
            self.czas_200.append(self.czas_wektory[i][2])
            self.czas_500.append(self.czas_wektory[i][3])
            self.czas_1000.append(self.czas_wektory[i][4])
            self.czas_2000.append(self.czas_wektory[i][5])

    # metoda licząca statystyki w każdej z wydzielonych wcześniej tabel
    def stat_sort(self):
        args=[self.czas_50,self.czas_100,self.czas_200,self.czas_500,self.czas_1000,self.czas_2000]

        # pętla dla każdej z tabel liczy jej statystyki i dodaje do tabeli statycstycznych
        for wektory in args:
            self.mins.append(min(wektory))
            self.maxs.append(max(wektory))
            self.means.append(sum(wektory)/len(wektory))

# w celu sprawdzenia czy sortowania działają należy zrobić coś takiego print(bubble_sort(jakas_tablica)[1]), gdyż funkcje sortujące zwracają wynik w takiej postaci (czas,posortowana_tablica), wtedy posortowana tablica znajduje się pod indeksem 1, taka typ danych nazywa się tuple
def bubble_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)
    zamiana = False
    for i in range(l - 1):
        for j in range(0, l - i - 1):
            if wektor[j] > wektor[j + 1]:
                zamiana = True
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
    if not zamiana:
        return
    end = tm.perf_counter_ns()
    czas_bubble_sort = end - start
    return czas_bubble_sort, wektor

def selection_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)
    for i in range(0, l - 1):
        min_ind = 0
        for j in range(i + 1, l):
            if wektor[j] < wektor[min_ind]:
                min_ind = j
        wektor[i], wektor[min_ind] = wektor[min_ind], wektor[i]

    end = tm.perf_counter_ns()
    czas_sel_sort = end - start
    return czas_sel_sort, wektor

def insertion_sort(wektor):
    start: int = tm.perf_counter_ns()
    l = len(wektor)
    for i in range(1, l):
        k = wektor[i]
        ind_posort = i - 1
        while k < wektor[ind_posort] and ind_posort >= 0:
            wektor[ind_posort + 1] = wektor[ind_posort]
            ind_posort = ind_posort - 1
        wektor[ind_posort + 1] = k

    end = tm.perf_counter_ns()
    czas_ins_sort = end - start
    return czas_ins_sort, wektor

def generowanie_wektorow():
    bubble_wektory = []
    insert_wektory = []
    selection_wektory = []
    for i in range(0, len(rozmiary)):
        temporary = [randint(0, 5000) for _ in range(0, rozmiary[i])]
        bubble_wektory.append(temporary.copy())
        insert_wektory.append(temporary.copy())
        selection_wektory.append(temporary.copy())
    return bubble_wektory,insert_wektory,selection_wektory


bubble_czas = []
insert_czas = []
selection_czas = []
rozmiary = [50, 100, 200, 500, 1000, 2000]

# 100 krotne powtórzenie sortowań (Metoda Monte Carlo)
for i in range(0,10):
    bubble_wektory,insertion_wektory,selection_wektory=generowanie_wektorow() # tworzenie nowych wektorów próbek dla każdego sortowania
    bubble_czas.append([bubble_sort(bubble_wektory[i])[0] for i in range(0, 6)]) # w każdej iteracji do tabeli czasów dodawane są kolejne czasy sortowania dla każdego rozmiaru tabeli wejściowej
    insert_czas.append([insertion_sort(insertion_wektory[i])[0] for i in range(0, 6)])
    selection_czas.append([selection_sort(selection_wektory[i])[0] for i in range(0, 6)])

# inicjalizacja klasy Results dla wszystkich sortowań, ważne, żeby podać czasy! Klasa sama wyznaczy sobie już wszystko, chillerka :)
bubble=Wyniki(bubble_czas)
insertion=Wyniki(insert_czas)
selection=Wyniki(selection_czas)

plt.figure(1)
plt.plot(rozmiary, bubble.means, label="Bubble sort średni czas")
plt.plot(rozmiary, insertion.means, label="Insertion sort średni czas")
plt.plot(rozmiary, selection.means, label="Selection sort średni czas")
plt.title("Średni czas algorytmów sortujących")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(rozmiary, bubble.mins, label="mins", s=10)
plt.scatter(rozmiary, bubble.maxs, label="maxs", s=10)
plt.scatter(rozmiary, bubble.means, label="means", s=10)
plt.title("Statystyki bubble sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(rozmiary, insertion.mins, label="mins", s=10)
plt.scatter(rozmiary, insertion.maxs, label="maxs", s=10)
plt.scatter(rozmiary, insertion.means, label="means", s=10)
plt.title("Statystyki insertion sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(rozmiary, selection.mins, label="mins", s=10)
plt.scatter(rozmiary, selection.maxs, label="maxs", s=10)
plt.scatter(rozmiary, selection.means, label="means", s=10)
plt.title("Statystyki selection sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.show()

tabela={
    "Bubble sort": bubble_czas,
    "Inserion sort": insertion_czas,
    "Selection sort": selection_czas
}
df = pd.DataFrame(tabela, index = rozmiary)
print(tbl.tabulate({"Rozmiary": rozmiary,"Bubble sort [ns]": bubble_czas,"Inserion sort [ns]": insertion_czas,"Selection sort [ns]": selection_czas}, headers="keys", tablefmt="mixed_grid"))
