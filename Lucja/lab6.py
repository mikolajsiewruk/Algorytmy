import numpy as np
import random
import time as tm
import matplotlib.pyplot as plt

class Results:
    def __init__(self, time_arr):
        super().__init__()
        self.time_arr=time_arr
        self.time50 = []
        self.time100 = []
        self.time200 = []
        self.time500 = []
        self.time1000 = []
        self.time2000 = []
        self.mins=[]
        self.maxs=[]
        self.means=[]
        self.separate_arrays()
        self.get_stats()
class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewa = None
        self. prawa = None


class BST: #drzewo przeszukiwań binarnych
    def __init__(self, tablica: list):
        self.wektor = tablica
        self.korzen = Wezel(self.wektor[0])
        self.drzewo()  #automatycznie tworzenie drzew z wartości podanych w tabeli

    def drzewo(self):
        for numery in self.wektor[1:]:
            self.insert(self.korzen, numery)

    def wstawianie(self, wezel, wartosc): #wstawianie elementu
        if wezel.wartosc:
            if wartosc > wezel.wartosc:  #jeśli jest większe to wstaw z prawej
                if wezel.prawy is None:
                    wezel.prawy = Wezel(wartosc)
                else:
                    self.insert(wezel.prawy, wartosc)
            else:  #jesli mniejsze to wstaw z lewej
                if wezel.lewy is None:  #jeśli nie ma lewego węzła to wstaw
                    wezel.lewy = Wezel(wartosc)
                else:  # jeśli jest to kontynuuj
                    self.insert(wezel.lewy, wartosc)
        else:
            wezel.wartosc = wartosc

    def usuwanie(self, wezel, wartosc):
        if wezel is self.Korzen:
            self.deleteKorzen()
            return
        else:
            if wezel.prawy is None and wezel.lewy is None: #jesli nie ma zadnego wezla to usun go
                self.deletewezel()
                return
            if wezel.prawy is None and wezel.lewy is not None: #jesli w prawym wezle jest nic a w lewym cos to usun lewy
                self.delete(wezel.lewy, wartosc)
                return
            if wezel.right is not None and wezel.left is None: #jesli w prawym wezle jest cos a w lewym nie to usun
                self.delete(wezel.prawy,wartosc)
                return
            if wezel.right is not None and wezel.left is not None: #jesli w obu cos jest to usun z lewego
                self.delete(wezel.lewy, wartosc)
                return

    def wyszukiwanie(self, wezel, wartosc): #wyszukiwanie elementu
        if not wezel:
            return False
        else:
            if wezel.value == wartosc:
                return wezel
            else:
                if wartosc > wezel.value:
                    if wezel.prawy == None:
                        return 1
                    else:
                        return self.wyszukiwanie(wezel.prawy, wartosc)
                else:
                    if wezel.left == None:
                        return 1
                    else:
                        return self.wyszukiwanie(wezel.prawy, wartosc)
    def minimum(self, wezel): #wyszukiwanie elementu najmniejszego
        if wezel:
            if wezel.lewy is not None:
                return self.minimum(wezel.lewy)
            else:
                return wezel
        else:
            return 1

    def maksimum(self, wezel): #wyszukiwanie elementu najwiekszego
        if wezel:
            if wezel.prawy is not None:
                return self.maksimum(wezel.prawy)
            else:
                return wezel
        else:
            return 1

    def poprzednik(self, wartosc): #wyszukiwanie poprzednika
        Korzen = self.wyszukiwanie(self.korzen, wartosc)
        if Korzen.lewy:
            return self.maksimum(Korzen.lewy)
        else:
            return "Nie istnieje lewe poddrzewo"

    def nastepnik(self, wartosc): #wyszukiwanie następnika
        Korzen = self.wyszukiwanie(self.korzen, wartosc)
        if Korzen.prawy:
            return self.minimum(Korzen.prawy)
        else:
            return "Nie istnieje prawe poddrzewo"


class AVL(BST):
    def __init__(self, wartosc):
        super().__init__(wartosc)

    def spr(self, wezel):
        if wezel is None:
            return 0
        else:
            return max(self.wysokość(wezel.lewy), self.wysokość(wezel.prawy)) + 1

    def rotacja_prawa(self, wezel): #zamienia wezel z lewym potomkiem
        P = wezel.lewy
        wezel.lewy = P.prawy
        P.prawy = wezel
        return P

    def rotacja_lewa(self, wezel): #zamienia wezel z prawym potomkiem
        L = wezel.prawy
        wezel.prawy = L.lewy
        L.lewy = wezel
        return L

    def rownowaga(self, wezel):
        if wezel is None:
            return wezel
        zrownowazenie = self.wysokosc(wezel.lewy) - self.wysokosc(wezel.prawy)
        if zrownowazenie > 1: #jesli zrownowazenie >1 to rotuj w prawo aby przywrocic zrownowazenie
            if self.wysokosc(wezel.lewy.lewy) >= self.wysokosc(wezel.lewy.prawy):
                return self.rotacja_w_prawo(wezel)
            else:
                wezel.lewy = self.rotacja_w_lewo(wezel.lewy)
                return self.rotacja_w_prawo(wezel)
        elif zrownowazenie < -1: #jesli zrownowazenie <-1 to rotuj w lewo
            if self.wysokosc(wezel.prawy.prawy) >= self.wysokosc(wezel.prawy.lewy):
                return self.rotacja_w_lewo(wezel)
            else:
                węzeł.prawy = self.rotacja_w_prawo(wezel.prawy)
                return self.rotacja_w_lewo(wezel)
        return węzeł

    def wstawienie(self, wezel, wartosc):
        if wezel is None:
            return WezelDrzewa(wartosc)
        elif wartosc < wezel.wartosc:
            węzeł.lewy = self.wstawienie(wezel.lewy, wartosc)
        else:
            węzeł.prawy = self.wstawienie(wezeł.prawy, wartosc)

        return self.zrownowazenie(wezel)

    def usuniecie(self, wezel, wartosc):
        if wezel is None: #jesli wezel jest pusty nie ma nic co usuniecia
            return wezel
        if wartosc < węzel.wartosc:
            węzel.lewy = self.usuniecie(węzel.lewy, wartosc) #jesli wartosc mniejsza niz wart wezla usuwamy lewego potomka
        elif wartosc > wezel.wartosc:
            wezel.prawy = self.usuniecie(wezel.prawy, wartosc) #jesli wartosc wieksza od wart wezlausuwamy prawego potomka
        else:
            if wezel.lewy is None:
                return węzeł.prawy #zwracamy prawy wezel i usuwamy
            elif wezel.prawy is None:
                return wezel.lewy #zwracamy lewy wezel i usuwamy
            temp = self.min_wartosc_wezla(wezel.prawy)
            wezel.wartosc = temp.wartosc
            węzeł.prawy = self.usuniecie(wezel.prawy, temp.wartosc)
        return self.zrownowazenie(wezel)

    def szukanie(self, wezel, wartosc):
        if wezel is None or wezel.wartosc == wartosc:
            return węzeł
        if wezel.wartosc< wartosc:
            return self.szukanie(wezel.prawy, wartosc) #przechodzimy do prawego poddrzewa
        else:
            if wezel.wartosc > wartosc:
                return self.szukanie(wezel.lewy, wartosc)
        return self.szukanie(wezel.lewy, wartosc) #w przeciwnym wypadku idziemy do lewego poddrzewa

    def min(self, wezel):
        obecny = wezel
        while obecny.lewy is not None:
            obecny = obecny.lewy
        return obecny

    def maks(self, wezel):
        obecny = wezel
        while obecny.prawy is not None:
            obecny = obecny.prawy
        return obecny

    def poprzedni(self, wartosc): #wyszukiwanie poprzednika
        Korzen = self.szukanie(self, wezel, wartosc)
        if Korzen.lewy:
            return self.maksimum(Korzen.lewy)
        else:
            return "Nie istnieje lewe poddrzewo"

    def nastepny(self, wartosc): #wyszukiwanie następnika
        Korzen = self.szukanie(self, wezel, wartosc)
        if Korzen.prawy:
            return self.minimum(Korzen.prawy)
        else:
            return "Nie istnieje prawe poddrzewo"

def generowanie():
    sizes = [50, 100, 200, 500, 1000, 2000]
    bst_wektor = []
    avl_wektor = []
    wektor = []
    for j in range(len(sizes)):
        for i in range(1, sizes[j]+1):
            wektor.append(i)
        np.random.shuffle(wektor)
        temp = wektor.copy()
        bst_wektor.append(temp)
        avl_wektor.append(temp)
    return bst_wektor, avl_wektor


sizes = [50, 100, 200, 500, 1000, 2000]
time_bst = []
time_avl = []

for k in range(100):
    wektor = generowanie()
    t_bst = []
    t_avl = []
    for i in range(len(sizes)):
        bst = BST(wektor[0][i])
        avl = AVL(wektorr[1][i])

        wartosci = []
        time_bst_temp = 0
        time_avl_temp = 0

        for j in range(100):
            wartosci.append(random.randint(1, sizes[i]))

        for wart in wartosci:
            t1 = tm.perf_counter_ns()
            bst.search(bst.korzen,wart)
            t2 = tm.perf_counter_ns()
            time_bst_temp += t2-t1

            t3 = tm.perf_counter_ns()
            avl.search(avl.korzen,wart)
            t4 = tm.perf_counter_ns()
            time_avl_temp += t4-t3

        t_bst.append(time_bst_temp)
        t_avl.append(time_avl_temp)
    time_bst.append(t_bst)
    time_avl.append(t_avl)

stats_avl = Results(time_avl)
stats_bst = Results(time_bst)

plt.plot(sizes,stats_avl.mean, label = "Drzewo AVL")
plt.plot(sizes,stats_bst.mean, label = "Drzewo BST")
plt.title("Porównanie czasów przeszukania elementów dla BST i AVL")
plt.xlabel("Długość wektora")
plt.ylabel("Średni czas przeszukiwania")
plt.grid()
plt.legend()
plt.show()