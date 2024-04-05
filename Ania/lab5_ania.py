class Wezel1: # definicja klasy wezel
    def __init__(self,wartosc):
        self.wartosc = wartosc
        self.lewa = None # początkowa wartość jest pusta
        self.prawa = None

    def wstawianie_wartosci_lewego_liscia(self, wartosc): # definicja metody do wstawiania wartosci lewego i prawego liscia liscia
        self.lewa = wartosc

    def wstawianie_wartosci_prawego_liscia(self, wartosc):
        self.prawa = wartosc

    def wstawianie_wartosci_lewego_wezla(self, wartosc):  # definicja metody do wstawiania wartosci lewego i prawego wezla
        self.lewa = Wezel1(wartosc)

    def wstawianie_wartosci_prawego_wezla(self, wartosc):
        self.prawa = Wezel1(wartosc)

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

class Drzewo:
    def __init__(self,wektor):
        self.wektor = wektor
        self.korzen = Wezel(wektor[0])

    def tworzenie_drzewa(self):
        for i in range (1, len(self.wektor)):
            self.korzen.wstawianie(self.wektor[i])

class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewa = None
        self.prawa = None

    def wstawianie(self, wartosc):
        if self.wartosc:
            if wartosc < self.wartosc:
                if self.lewa is None:
                    self.lewa = Wezel(wartosc)
                else:
                    self.lewa.wstawianie(wartosc)
            elif wartosc > self.wartosc:
                if self.prawa is None:
                    self.prawa = Wezel(wartosc)
                else:
                    self.prawa.wstawianie(wartosc)
        else:
            self.wartosc = wartosc

    def pobierz_wartosc(self):
        print(self.warotsc)

    def wyswietlanie_drzewa(self):
        if self.lewa:
            self.lewa.wyswietlanie_drzewa()
        if self.prawa:
            self.prawa.wyswietlanie.drzewa()



a = Drzewo ([20,5,13,18,189,249])
a.tworzenie_drzewa()



