import random as rnd
import time as tm
import matplotlib.pyplot as plt


def bubble_sort(wektor1):
    start:int=tm.perf_counter_ns()
    l=len(wektor1) #długość wektora
    zamiana=False
    for i in range(l-1): #Idziemy przez wektor od początku do przedostatniego elementu
                         #ostatni element pomijamy, bo nie ma go z czym porównać
        for j in range(0, l-i-1): #przechodzimy przez sąsiednie pary elementów
            if wektor1[j]>wektor1[j+1]: #sprawdzamy czy element po lewej jest większy od tego po prawej
                zamiana=True #jeżeli tak następuje zamiana miejsc
                wektor1[j], wektor1[j+1] = wektor1[j+1], wektor1[j]
    if not zamiana: #jeżeli nie nastąpiła żadna zamiana to lista została posortowana
        return
    end=tm.perf_counter_ns()
    czas_bubble_sort=end-start
    return czas_bubble_sort, wektor1

def selection_sort(wektor2):
    start=tm.perf_counter_ns()
    l=len(wektor2)
    for i in range (0,l):
        min_el=0  #przypisanie że pierwszy indeks ma wartość element o najmniejszej wartość
        for j in range (0, l-i):
            if wektor2[j]>min_el: #sprawdzamy czy kolejny element jest mniejszy od naszego min_el
                min_el=wektor2[j]
                wektor2[wektor2.index(min_el)], wektor2[-1-j]=wektor2[-1-j], wektor2[wektor2.index(min_el)] # jeżeli tak, nastepuje zamiana miejsc

    end=tm.perf_counter_ns()
    czas_sel_sort=end-start
    return czas_sel_sort, wektor2

def insertion_sort(wektor3):
    start=tm.perf_counter_ns()
    l=len(wektor3)
    for i in range(1, l):
        sp=wektor3[i]
        ind_posort=i-1
        while sp<wektor3[ind_posort] and ind_posort>=0:
            wektor3[ind_posort+1]=wektor3[ind_posort]
            ind_posort=ind_posort-1
        wektor3[ind_posort+1]=sp

    end=tm.perf_counter_ns()
    czas_ins_sort=end-start
    return czas_ins_sort, wektor3



def generowanie_wektorow(N,minimum,maksimum): # wazne zeby tu dodac argumenty tej funkcji oraz przy jej uruchamianiu tez je podac

    for i in range(0, len(sizes)): # tu zmienic na N
        temporary = [rnd.randint(0, 5000) for _ in range(0, sizes[i])] # to zmienic tak zeby temp bylo tylko jedna liczba, zakres randint(minimum,maksimum)
        bubble_wektory.append(temporary.copy())
        insert_wektory.append(temporary.copy())
        selection_wektory.append(temporary.copy())
    return bubble_wektory,insert_wektory,selection_wektory

bubble_wektory = []
insert_wektory = []
selection_wektory = []
czas_bubble = []
czas_ins = []
czas_sel = []
sizes = [50, 100, 200, 500, 1000, 2000]
w1,w2,w3=generowanie_wektorow() # BARDZO WAŻNE!!!, tak się odwołuje do rezultatów generowania wektora w tej postaci co teraz dodałem

for i in range(0,6):
    czas_bubble.append(bubble_sort(w1[i])[0])
    czas_ins.append(insertion_sort(w2[i])[0])
    czas_sel.append(selection_sort(w3[i])[0])

def rysowanie_wykresu():
    plt.plot([50, 100, 200, 1000, 2000, 5000], czas_bubble, label="Sortowanie bombelkowe")
    plt.plot([50,100,200,1000,2000,5000],czas_ins, label="Sorotwanie przez wstawianie")
    plt.plot([50, 100, 200, 1000, 2000, 5000], czas_sel, label="Sortowanie przez wybór")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas sortowania [nanosekundy]")
    plt.title("Porównanie czasu sortowania algorytmów")
    plt.legend()
    plt.grid(True)
    plt.show()
rysowanie_wykresu()