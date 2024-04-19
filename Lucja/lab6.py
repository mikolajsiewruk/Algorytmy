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
