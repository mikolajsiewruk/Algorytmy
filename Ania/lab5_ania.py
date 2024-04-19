from random import randint
import time as tm
import matplotlib.pyplot as plt
class Wezel: # definicja klasy wezel
    def __init__(self,wartosc):
        self.wartosc = wartosc
        self.lewa = None # początkowa wartość jest pusta
        self.prawa = None

    def wstawianie_wartosci_lewego_liscia(self, wartosc): # definicja metody do wstawiania wartosci lewego i prawego liscia liscia
        self.lewa = wartosc

    def wstawianie_wartosci_prawego_liscia(self, wartosc):
        self.prawa = wartosc

    def wstawianie_wartosci_lewego_wezla(self, wartosc):  # definicja metody do wstawiania wartosci lewego i prawego wezla
        self.lewa = Wezel(wartosc)

    def wstawianie_wartosci_prawego_wezla(self, wartosc):
        self.prawa = Wezel(wartosc)

    def uzyskiwanie_wartosci_lewej(self): # definicja metody do uzyskiwania wartosci
        if type (self.lewa) == int:
            return self.lewa
        else:
            return self.lewa.wartosc

    def uzyskiwanie_wartosci_prawej(self):
        if type (self.prawa) == int:
            return self.prawa
        else:
            return self.prawa.wartosc
    def wyswietlanie_drzewa(self):
        if self.lewa:
            self.lewa.wyswietlanie_drzewa()
        print(self.wartosc)
        if self.prawa:
            self.prawa.wyswietlanie_drzewa()

a = Wezel(5)
a.wstawianie_wartosci_lewego_wezla(3)
a.wstawianie_wartosci_prawego_wezla(17)
a.lewa.wstawianie_wartosci_lewego_wezla(48)
a.lewa.wstawianie_wartosci_prawego_wezla(4)
a.prawa.wstawianie_wartosci_lewego_wezla(256)
a.prawa.wstawianie_wartosci_prawego_wezla(82)
a.wyswietlanie_drzewa()
class DrzewoBin:
    def __init__(self, wektor):
        self.wektor = wektor
        self.korzen = Wezel(wektor[0])
    def dodawanie_wezla(self,wezel,wartosc):

        q = [] # kolejka węzłów do sprawdzenia
        q.append(wezel) # funkcja dodaje węzły do lewej
        while q:   # metoda dodaje nołdy od lewej, jeśli chcemy od prawej to trzeba zamienić ify kolejnością
            current=q[0]
            q.pop(0)
            if not current.lewa: # funkcja sprawdzająca czy węzeł ma lewą stronę
                print(f"{current.wartosc}  dodano {wartosc} do lewego węzła")
                current.lewa=Wezel(wartosc) # jeżeli nie, to dodawany jest lewy węzeł i kończy sprawdzanie
                break
            else:
                q.append(current.lewa)
            if not current.prawa: # funkcja sprawdzająca czy węzeł ma prawą stronę
                print(f"{current.wartosc}  dodano {wartosc} do prawego węzła")
                current.prawa=Wezel(wartosc) # jeżeli nie, to dodawany jest prawy węzeł i kończy sprawdzanie
                break
            else:
                q.append(current.prawa)
    def make_tree(self):

        for i in range(1,len(self.wektor)):
            self.dodawanie_wezla(self.korzen,self.wektor[i])

    def print_tree(self, wezel):
        if not wezel:
            return
        self.print_tree(wezel.left)
        print(wezel.wartosc, end=" ")
        self.print_tree(wezel.prawa)
class Wyniki: # algorytmy wklejone z lab4
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

    # funkcja, która wydoboywa czas sortowania wektora o danym rozmiarze
    def oddzielne_wektory(self):
        for i in range(0,len(self.czas_wektory)):
            self.czas_50.append(self.czas_wektory[i][0])
            self.czas_100.append(self.czas_wektory[i][1])
            self.czas_200.append(self.czas_wektory[i][2])
            self.czas_500.append(self.czas_wektory[i][3])
            self.czas_1000.append(self.czas_wektory[i][4])
            self.czas_2000.append(self.czas_wektory[i][5])

    # obliczanie statystyk
    def stat_sort(self):
        args=[self.czas_50,self.czas_100,self.czas_200,self.czas_500,self.czas_1000,self.czas_2000]
        for wektory in args:
            self.mins.append(min(wektory))
            self.maxs.append(max(wektory))
            self.means.append(sum(wektory)/len(wektory))
class Sorter:
    def __init__(self):
        self.merge_sorted = []
        self.counting_sorted = []
        self.quick_sorted = []
        self.heap_sorted = []

    def merge_sort(self, wektor): # złożoność liniowo-logarytmiczna Θnlog(n)
        if len(wektor)>1:
            srodek=(len(wektor) // 2) #wyznaczanie środka wektora
            lewa = wektor[:srodek] # podzielenie wektora na część lewą i prawą
            prawa = wektor[srodek:]
            self.merge_sort(lewa) # rekurencyjne wywoływanie dla każdej połowy
            self.merge_sort(prawa)

            i=j=k=0 # początkowe indeksy tablic

            while i < len(lewa) and j < len(prawa):
                # porównywanie elementów lewej i prawej części wektora
                if lewa[i] < prawa[j]: # jezeli elemeny jest mniejszy w części lewej to umieszczamy go w tablicy docelowej
                    wektor[k] = lewa[i]
                    i += 1 # zwiększamy indeks tablicy lewej części
                else:
                    wektor[k] = prawa[j]
                    j += 1 # zwiększamy indeks tablicy prawej części
                k += 1 # zwiększamy indeks tablicy docelowej

            # kopiowanie pozostałych elementów z obu części
            while i < len(lewa):
                wektor[k] = lewa[i]
                i += 1
                k += 1

            while j < len(prawa):
                wektor[k] = prawa[j]
                j += 1
                k += 1
        return wektor

    def counting_sort(self, wektor): # złożoność Θ (n+m), n - liczba elementów w wektorze, k - zakres wartości elementów
        maks=max(wektor) # znalezienie największej weartości w wektorze
        mini=min(wektor) # znalezienie najmniejszej weartości w wektorze
        posort=[] # tablica na posortowane elementy
        k=[0]*(maks+1) # lista zer, jej długość jest ustalana na podstawie maksymalnej wartości w wektorze zwiększonej o 1
        for i in range(len(wektor)): #przechodzenie przez całą długość wektora
            k[wektor[i]]= k[wektor[i]] + 1 # zwiększenie liczby wystąpień danego elementu wektora tablizy z zeramo o 1
        for j in range(len(k)): # przechodzimy przez listę zer
            if k[j]!=0: # jeżeli element j jest różny od 0, to dodajemy go do posortowanej części
                posort.append(j)
        return posort

    def quick_sort(self, wektor):
        if len(wektor)>1:
            pivot = wektor[-2]
            l = 0
            r = len(wektor) - 1
            while l < r:
                if wektor[l] > pivot and wektor[r] < pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                elif wektor[l] == pivot and wektor[r] < pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                    l += 1
                elif wektor[r] == pivot and wektor[l] > pivot:
                    wektor[l], wektor[r] = wektor[r], wektor[l]
                    r -= 1
                elif wektor[l] >= pivot:
                    r -= 1
                elif wektor[r] <= pivot:
                    l += 1
                else:
                    l += 1
                    r -= 1
            c = wektor.count(pivot)
            left = wektor[:wektor.index(pivot) + c]
            right = wektor[wektor.index(pivot) + c:]
            if not left or not right:
                wektor = left + right
                return wektor
            a = self.quick_sort(left)
            b = self.quick_sort(right)
            wektor = a + b
        return wektor


# funkcja pomocnicza sprawdzająca czy dany węzeł ma cechę kopca
    def heapify(self, wektor, N, i): # N - wielkość tablicy, i - indeks sprawdzanego elementu
        największe = i  # inicjalizacja największego jako korzeń
        l = 2 * i + 1  # lewe dziecko
        p = 2 * i + 2  # prawe dziecko

        if l < N and wektor[największe] < wektor[l]: # sprawdzanie czy lewe dziecko korzenia istnieje i czy jest od niego większe
            największe = l

        if p < N and wektor[największe] < wektor[p]: # sprawdzanie czy prawe dziecko korzenia istnieje i czy jest od niego większe
            największe = p

        if największe != i: # jeżeli dziecko jest większe od korzenia następuje zamiana
            wektor[i], wektor[największe] = wektor[największe], wektor[i]

            self.heapify(wektor, N, największe)
    def heapsort(self, wektor):
        N = len(wektor)
        for i in range(N // 2 - 1, -1, -1): # budowanie kopca od końca tablicy
            self.heapify(wektor, N, i)

        for i in range(N - 1, 0, -1): # zamiana elementów od tyłu
            wektor[i], wektor[0] = wektor[0], wektor[i]
            self.heapify(wektor, i, 0)
        return wektor
def generowanie_wektorow():
    merge_wektory = []
    counting_wektory = []
    quick_wektory = []
    heap_wektory = []
    for i in range(0, len(rozmiary)):
        temporary = [randint(0, 5000) for _ in range(0, rozmiary[i])]
        merge_wektory.append(temporary.copy())
        counting_wektory.append(temporary.copy())
        quick_wektory.append(temporary.copy())
        heap_wektory.append(temporary.copy())
    return merge_wektory,counting_wektory,quick_wektory, heap_wektory

merge_czas = []
counting_czas = []
quick_czas = []
heap_czas = []
rozmiary = [50, 100, 200, 500, 1000, 2000]
sorter=Sorter()

# Metoda Monte Carlo
for i in range(0,100):
    merge_wektory, counting_wektory, quick_wektory, heap_wektory = generowanie_wektorow()
    m_temp = []
    c_temp = []
    q_temp = []
    h_temp = []
    for j in range(6):
        m_start = tm.perf_counter_ns()
        sorter.merge_sort(merge_wektory[j])
        m_end = tm.perf_counter_ns()
        m_temp.append(m_end - m_start)

        c_start = tm.perf_counter_ns()
        sorter.counting_sort(counting_wektory[j])
        c_end = tm.perf_counter_ns()
        c_temp.append(c_end - c_start)

        q_start = tm.perf_counter_ns()
        sorter.quick_sort(quick_wektory[j])
        q_end = tm.perf_counter_ns()
        q_temp.append(q_end - q_start)

        h_start = tm.perf_counter_ns()
        sorter.heapsort(heap_wektory[j])
        h_end = tm.perf_counter_ns()
        h_temp.append(h_end - h_start)

    merge_czas.append(m_temp)
    counting_czas.append(c_temp)
    quick_czas.append(q_temp)
    heap_czas.append(h_temp)

merge=Wyniki(merge_czas)
counting=Wyniki(counting_czas)
quick=Wyniki(quick_czas)
heap=Wyniki(heap_czas)


plt.figure(1)
plt.plot(rozmiary, merge.means, label="Merge sort średni czas")
plt.plot(rozmiary, counting.means, label="Counting sort średni czas")
plt.plot(rozmiary, quick.means, label="Quick sort średni czas")
plt.plot(rozmiary,heap.means, label="Heap sort średni czas")
plt.title("Średni czas algorytmów sortujących")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(2)
plt.scatter(rozmiary, merge.mins, label="min", s=10)
plt.scatter(rozmiary, merge.means, label="śr", s=10)
plt.scatter(rozmiary, merge.maxs, label="max", s=10)
plt.title("Statystyki merge sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(3)
plt.scatter(rozmiary, counting.mins, label="min", s=10)
plt.scatter(rozmiary, counting.means, label="śr", s=10)
plt.scatter(rozmiary, counting.maxs, label="max", s=10)
plt.title("Statystyki counting sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.figure(4)
plt.scatter(rozmiary, quick.mins, label="min", s=10)
plt.scatter(rozmiary, quick.means, label="śr", s=10)
plt.scatter(rozmiary, quick.maxs, label="max", s=10)
plt.title("Statystyki quick sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.show()

plt.figure(5)
plt.scatter(rozmiary,heap.mins,label="min",s=10)
plt.scatter(rozmiary,heap.means,label="śr",s=10)
plt.scatter(rozmiary,heap.maxs,label="max",s=10)
plt.title("Statystyki heap sort'a dla różnych rozmiarów wektora")
plt.xlabel("Rozmiar wektora")
plt.ylabel("Czas sortowania")
plt.legend()
plt.grid(True)

plt.show()

