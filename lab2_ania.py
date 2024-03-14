import random as rnd
import time as tm
import matplotlib.pyplot as plt


def generowanie_wektora():
    bubble_arrays = []
    insert_arrays = []
    selection_arrays = []
    for i in range(0, len(sizes)):
        temporary = [rnd.randint(0, 5000) for _ in range(0, sizes[i])]
        bubble_arrays.append(temporary.copy())
        insert_arrays.append(temporary.copy())
        selection_arrays.append(temporary.copy())
    return bubble_arrays,insert_arrays,selection_arrays
def bubble_sort(wektor1):
    start:int =tm.perf_counter_ns()
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
    start = tm.perf_counter_ns()
    l=len(wektor2)
    for i in range (l):
        min_el=wektor2[i]  #przypisanie że pierwszy indeks ma wartość element o najmniejszej wartość
        for j in range (i+1, l):
            if wektor2[j]<wektor2[i]: #sprawdzamy czy kolejny element jest mniejszy od naszego min_el
                min_el=j
                wektor2[i], wektor2[min_el]=wektor2[min_el], wektor2[i] # jeżeli tak, nastepuje zamiana miejsc

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

# zastapilem funkcje generujaca petla for i troche inna struktura, jesli nie ma kopii pomiedzy w1,w2 i w3 to sortowanie jednego z nich nie zmieni innych
sizes = [50, 100, 200, 500, 1000, 2000]
w1,w2,w3=generowanie_wektora() # BARDZO WAŻNE!!!, tak się odwołuje do rezultatów generowania wektora w tej postaci co teraz dodałem

czas_bubble=[]
czas_ins=[]
czas_sel=[]

for i in range(0,6):
    czas_bubble.append(bubble_sort(w1[i])[0])
    czas_ins.append(insertion_sort(w2[i])[0])
    czas_sel.append(selection_sort(w3[i])[0])
'''wektor_podany=generowanie_wektora(min, max)
print(wektor_podany)'''

print(czas_ins)

N=int(input("Podaj długość wektora: "))
min=int(input("Podaj minimalną wartość wektora: "))
max=int(input("Podaj maksymalną wartość wektora: "))

'''wektor=generowanie_wektora(min,max) # moja funkcja generująca wektor zwraca cos takiego result=[[1,2,3],[4,5,65],[69,2137,420]], żeby się odwolac do 1 tablicy to result[0] zeby sie odwolac do 69 result[2][0]
wektor1=wektor.copy()
wektor2=wektor.copy()
wektor3=wektor.copy(


# tutaj wszystkie wyniki są złe ponieważ sortując 1 tabele sortuja sie jej wszystkie kopie

czas_bubble_sort=bubble_sort(wektor1[0])[0]

print("Wektor posortowany przy użyciu sortowania bąbelkowego: ", wektor1[0])
print("Czas sortowania:",czas_bubble_sort, "nanosekund")

czas_sel_sort=selection_sort(wektor2[0])[0]
print("Wektor posortowany przy użyciu sortowania poprzez wybór: ", wektor2[0])
print("Czas sortowania:",czas_sel_sort, "nanosekund")

czas_ins_sort=insertion_sort(wektor3[0])[0]
print("Wektor posortowany przy użyciu sortowania przez wstawianie: ", wektor3[0])
print("Czas sortowania:", czas_ins_sort, "nanosekund")'''

# koniec zlego kodu, wykres dziala
def rysowanie_wykresu():
    plt.plot([50, 100, 200, 1000, 2000, 5000], czas_ins, label="Insertion sort")
    plt.plot([50,100,200,1000,2000,5000],czas_bubble, label="Bubble sort")
    plt.plot([50,100,200,1000,2000,5000],czas_sel, label="Selection sort")
    plt.xlabel("Rozmiar wektora")
    plt.ylabel("Czas sortowania [nanosekundy]")
    plt.title("Porównanie czasu sortowania algorytmów")
    plt.legend()
    plt.grid(True)
    plt.show()
rysowanie_wykresu()
