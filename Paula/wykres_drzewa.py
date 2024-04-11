import random
import networkx as nx
import time
import matplotlib.pyplot as plt
# Punkt 1: Zaimplementowanie klasy drzewa binarnego

# Klasa definiująca węzeł drzewa binarnego
class WezelDrzewaBinarne:
    # Konstruktor węzła
    def __init__(self, klucz):
        # Przechowuje wartość klucza węzła
        self.klucz = klucz
        # Wskaźniki do lewego i prawego dziecka
        self.lewy = None
        self.prawy = None

# Klasa definiująca drzewo binarne
class DrzewoBinarne:
    # Konstruktor drzewa
    def __init__(self):
        # Korzeń drzewa
        self.korzen = None

    # Metoda do wstawiania wartości do drzewa
    def wstaw(self, klucz):
        # Jeśli drzewo jest puste, tworzymy korzeń
        if self.korzen is None:
            self.korzen = WezelDrzewaBinarne(klucz)
        else:
            # Rekurencyjne wstawianie wartości do drzewa
            self._wstaw_rekurencyjnie(self.korzen, klucz)

    # Metoda pomocnicza do rekurencyjnego wstawiania wartości
    def _wstaw_rekurencyjnie(self, wezel, klucz):
        # Jeśli węzeł nie ma lewego dziecka, wstawiamy tam nową wartość
        if wezel.lewy is None:
            wezel.lewy = WezelDrzewaBinarne(klucz)
        # Jeśli węzeł nie ma prawego dziecka, wstawiamy tam nową wartość
        elif wezel.prawy is None:
            wezel.prawy = WezelDrzewaBinarne(klucz)
        # W przeciwnym razie rekurencyjnie wstawiamy do lewego poddrzewa
        else:
            self._wstaw_rekurencyjnie(wezel.lewy, klucz)

    # Metoda do wyświetlania reprezentacji drzewa
    def wyswietl_drzewo(self):
        # Rekurencyjne wyświetlanie drzewa
        self._wyswietl_drzewo_rekurencyjnie(self.korzen, 0)

    # Metoda pomocnicza do rekurencyjnego wyświetlania drzewa
    def _wyswietl_drzewo_rekurencyjnie(self, wezel, poziom):
        # Jeśli węzeł nie jest pusty
        if wezel is not None:
            # Rekurencyjne wyświetlenie prawego poddrzewa
            self._wyswietl_drzewo_rekurencyjnie(wezel.prawy, poziom + 1)
            # Wyświetlenie wartości klucza węzła z wcięciami
            print("    " * poziom + str(wezel.klucz))
            # Rekurencyjne wyświetlenie lewego poddrzewa
            self._wyswietl_drzewo_rekurencyjnie(wezel.lewy, poziom + 1)


# Punkt 2: Generowanie losowego wektora 10-elementowego i tworzenie drzewa binarnego

# Generowanie wektora 10 losowych liczb z przedziału [0, 10]
wektor = [random.randint(0, 10) for _ in range(10)]

# Tworzenie pustego drzewa binarnego
drzewo = DrzewoBinarne()

# Wstawianie wszystkich wartości z wektora do drzewa
for klucz in wektor:
    drzewo.wstaw(klucz)

# Wyświetlanie reprezentacji drzewa binarnego
print("Drzewo Binarnego:")
drzewo.wyswietl_drzewo()

# Punkt 3: Klasa definiująca kopiec binarny

class DrzewoKopca:
    # Konstruktor kopca
    def __init__(self):
        # Lista przechowująca elementy kopca
        self.kopiec = []

    # Metoda do wstawiania elementu do kopca
    def wstaw(self, element):
        # Dodanie elementu na koniec listy
        self.kopiec.append(element)
        # Naprawa kopca od dołu do góry
        self.napraw_kopiec_gora(len(self.kopiec) - 1)

    # Metoda naprawiająca kopiec od dołu do góry
    def napraw_kopiec_gora(self, indeks):
        # Obliczenie indeksu rodzica
        rodzic = (indeks - 1) // 2
        # Warunek sprawdzający, czy element ma rodzica i czy jest od niego większy
        if indeks > 0 and self.kopiec[indeks] > self.kopiec[rodzic]:
            # Zamiana elementu z rodzicem
            self.kopiec[indeks], self.kopiec[rodzic] = self.kopiec[rodzic], self.kopiec[indeks]
            # Rekurencyjne wywołanie metody dla rodzica
            self.napraw_kopiec_gora(rodzic)

    # Metoda tworząca kopiec z listy elementów
    def stworz_kopiec(self, wektor):
        # Wstawianie każdego elementu z listy do kopca
        for element in wektor:
            self.wstaw(element)

    # Metoda wyświetlająca kopiec
    def wyswietl_kopiec(self):
        print("Kopiec:")
        # Wyświetlanie wszystkich elementów kopca
        for element in self.kopiec:
            print(element, end=" ")
        print()

    # Metoda sortująca kopiec
    def sortowanie_przez_kopcowanie(self):
        # Posortowana lista
        posortowane = []
        # Dopóki kopiec nie jest pusty
        while self.kopiec:
            # Zamiana pierwszego elementu z ostatnim
            self.kopiec[0], self.kopiec[-1] = self.kopiec[-1], self.kopiec[0]
            # Dodanie usuniętego elementu do posortowanej listy
            posortowane.insert(0, self.kopiec.pop())
            # Naprawa kopca od góry do dołu
            self.napraw_kopiec_dol(0)
        # Zwrócenie posortowanej listy
        return posortowane

    # Metoda naprawiająca kopiec od góry do dołu
    def napraw_kopiec_dol(self, indeks):
        # Obliczenie indeksów lewego i prawego dziecka
        lewy = 2 * indeks + 1
        prawy = 2 * indeks + 2
        # Zmienna przechowująca indeks elementu o największej wartości
        najwiekszy = indeks
        # Warunek sprawdzający, czy lewe dziecko istnieje i jest większe od elementu
        if lewy < len(self.kopiec) and self.kopiec[lewy] > self.kopiec[najwiekszy]:
            najwiekszy = lewy
        # Warunek sprawdzający, czy prawe dziecko istnieje i jest większe od elementu
        if prawy < len(self.kopiec) and self.kopiec[prawy] > self.kopiec[najwiekszy]:
            najwiekszy = prawy
        # Warunek sprawdzający, czy znaleziono element o większej wartości
        if najwiekszy != indeks:
            # Zamiana elementu z dzieckiem o największej wartości
            self.kopiec[indeks], self.kopiec[najwiekszy] = self.kopiec[najwiekszy], self.kopiec[indeks]
            # Rekurencyjne wywołanie metody dla dziecka o największej wartości
            self.napraw_kopiec_dol(najwiekszy)


# Punkt 4: Wygenerowanie losowego wektora 10-elementowego i przedstawienie go w postaci kopca
wektor_kopca = [random.randint(0, 10) for _ in range(10)]
kopiec = DrzewoKopca()
kopiec.stworz_kopiec(wektor_kopca)
kopiec.wyswietl_kopiec()

# Punkt 5: Implementacja algorytmu sortowania przez kopcowanie i jego zastosowanie do posortowania wygenerowanego wektora
posortowany_wektor_kopca = kopiec.sortowanie_przez_kopcowanie()
print("Posortowany wektor przez kopcowanie:", posortowany_wektor_kopca)

# Punkt 6: Analizując stworzony algorytm oszacuj klasę złożoności.
# Złożoność czasowa algorytmu sortowania przez kopcowanie wynosi O(n log n), gdzie n to liczba elementów w wektorze.
# Tworzenie kopca z losowego wektora o długości n wymaga O(n) operacji.
# Następnie sortowanie przez kopcowanie składa się z n kroków, gdzie w każdym kroku usuwamy największy element z korzenia kopca
# i naprawiamy kopiec (co wymaga przesunięcia w dół, co potencjalnie wymaga O(log n) operacji).
# Złożoność przestrzenna wynosi O(n), ponieważ kopiec zajmuje tyle samo miejsca co wejściowy wektor, z dodatkową zmienną pomocniczą dla sortowania.

# Punkt 7: Za pomocą wykresu porównaj złożoność algorytmu sortowania przez kopcowanie z algorytmami z laboratorium 4.
def sortowanie_przez_scalanie(lista):
    def scal(lista, pomocnicza, lewy, srodek, prawy):
        for i in range(lewy, prawy + 1):
            pomocnicza[i] = lista[i]
        i = lewy
        j = srodek + 1
        for k in range(lewy, prawy + 1):
            if i <= srodek:
                if j <= prawy:
                    if pomocnicza[j] < pomocnicza[i]:
                        lista[k] = pomocnicza[j]
                        j += 1
                    else:
                        lista[k] = pomocnicza[i]
                        i += 1

    def sortowanie(lista, pomocnicza, lewy, prawy):
        if lewy < prawy:
            srodek = (prawy + lewy) // 2
            sortowanie(lista, pomocnicza, lewy, srodek)
            sortowanie(lista, pomocnicza, srodek + 1, prawy)
            scal(lista, pomocnicza, lewy, srodek, prawy)

    pomocnicza = [0] * len(lista)
    sortowanie(lista, pomocnicza, 0, len(lista) - 1)


'''def sortowanie_przez_zliczanie(lista):
    min_w = min(lista)
    max_w = max(lista)
    count = [0] * (max_w - min_w + 1)
    for liczba in lista:
        count[liczba - min_w] += 1
    pos = 0
    for i in range(min_w, max_w + 1):
        for _ in range(count[i - min_w]):
            lista[pos] = i
            pos += 1


def sortowanie_szybkie(lista):
    def podzial(lista, dolny, gorny):
        pivot = lista[gorny]
        i = dolny - 1
        for j in range(dolny, gorny):
            if lista[j] <= pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[gorny] = lista[gorny], lista[i + 1]
        return i + 1

    def szybkie_sortowanie(lista, dolny, gorny):
        if dolny < gorny:
            pi = podzial(lista, dolny, gorny)
            szybkie_sortowanie(lista, dolny, pi - 1)
            szybkie_sortowanie(lista, pi + 1, gorny)

    szybkie_sortowanie(lista, 0, len(lista) - 1)


def generate_random_vector(size):
    return [random.randint(0, size) for _ in range(size)]


def measure_execution_time(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time


vector_sizes = [100, 1000, 5000, 10000]
kopiec_execution_times = []
merge_sort_execution_times = []
counting_sort_execution_times = []
quick_sort_execution_times = []

for size in vector_sizes:
    data = generate_random_vector(size)

    # Pomiar czasu wykonania sortowania przez kopcowanie
    kopiec = DrzewoKopca()
    kopiec_stworz_start = time.time()
    kopiec.stworz_kopiec(data)
    kopiec_stworz_end = time.time()
    kopiec_stworz_time = kopiec_stworz_end - kopiec_stworz_start

    kopiec_sort_start = time.time()
    kopiec.sortowanie_przez_kopcowanie()
    kopiec_sort_end = time.time()
    kopiec_sort_time = kopiec_sort_end - kopiec_sort_start

    kopiec_execution_times.append(kopiec_stworz_time + kopiec_sort_time)

    # Pomiar czasu wykonania algorytmu sortowania przez scalanie
    merge_sort_execution_times.append(measure_execution_time(sortowanie_przez_scalanie, data.copy()))

    # Pomiar czasu wykonania algorytmu sortowania przez zliczanie
    counting_sort_execution_times.append(measure_execution_time(sortowanie_przez_zliczanie, data.copy()))

    # Pomiar czasu wykonania algorytmu sortowania szybkiego
    quick_sort_execution_times.append(measure_execution_time(sortowanie_szybkie, data.copy()))

# Wykres złożoności czasowej w zależności od rozmiaru danych
plt.plot(vector_sizes, kopiec_execution_times, label='Sortowanie przez kopcowanieO(n log n)')
plt.plot(vector_sizes, merge_sort_execution_times, label='Sortowanie przez scalanieO(n log n)')
plt.plot(vector_sizes, counting_sort_execution_times, label='Sortowanie przez zliczanieO(n + k)')
plt.plot(vector_sizes, quick_sort_execution_times, label='Sortowanie szybkieO(n log n)')
plt.xlabel('Rozmiar danych')
plt.ylabel('Czas wykonania (s)')
plt.title('Porównanie złożoności czasowej różnych algorytmów sortowania')
plt.legend()
plt.show()'''


g=nx.Graph()
def generate_vector():
    t=[]
    used=[]
    while len(t)<10:
        a=random.randint(1,50)
        if a not in used:
            t.append(a)
            used.append(a)
    return t
vec=generate_vector()
def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
d=DrzewoKopca()
d.stworz_kopiec(vec)
x=d.korzen
pos = hierarchy_pos(g,f'{x.klucz}') # tutaj dodać root
nx.draw(g, pos=pos, with_labels=True)
plt.show()