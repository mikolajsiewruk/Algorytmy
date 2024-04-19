import random as rnd
import time as tm
import copy
import matplotlib.pyplot as plt
import pandas as pd

class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewa = None
        self.prawa = None

class BST:
    def __init__(self, wektor: list):
        self.wektor = wektor
        self.korzen = Wezel(self.wektor[0]) # Ustawienie korzenia drzewa na pierwszy element wektora

    def wstawianie(self, wezel, wartosc): # Wstawianie elementów
        if wezel.wartosc: # jeżeli węzęł ma przypisaną wartość
            if wartosc < wezel.wartosc: # jeżeli wstawiania wartośc jest mniejsza od przypisanej wartości
                if wezel.lewa is None:
                    wezel.prawa = Wezel(wartosc)
                else: # wstawiamy tą wartość po lewej stronie
                    self.wstawianie(wezel.lewa, wartosc)
            else:# Jeśli wstawiana wartość jest większa lub równa przypisanej wartości
                if wezel.prawa is None:
                    wezel.prawa = Wezel(wartosc)
                else: # wstawiamy tą wartość po prawej stronie
                    self.wstawianie(wezel.prawa, wartosc)
        else:
            wezel.wartosc = wartosc

    def usuwanie(self, wartosc):  # Usuwanie elementów
        wezel, rodzic = self.wyszukiwanie(self.korzen, wartosc) # wyszukiwanie węzłu i jego rodzica
        if wezel.wartosc:
            if wezel.lewa is None and wezel.prawa is None: # Brak dzieci
                if rodzic: # jeżeli węzeł ma rodzica
                    if rodzic.prawa is wezel: # jeżeli węzeł jest prawym dzieckiem
                        rodzic.prawa = None # usuwanie
                    else:
                        rodzic.lewa = None
                else:
                    self.korzen = None

    def wyszukiwanie(self, wezel, wartosc, rodzic=None):  # Wyszukiwanie elementu
        if not wezel: # jeżeli węzeł nie istnieje to brak elementów do wyszukania
            return False
        else: # Jeśli wartość węzła jest równa szukanej wartości
            if wezel.wartosc == wartosc:
                return wartosc, rodzic # następuje zwrócenie węzła i rodzica
            elif wartosc > wezel.wartosc: # Jeśli szukana wartość jest większa od wartość węzła
                return self.wyszukiwanie(wezel.prawa, wartosc, wezel) # wyszukiwanie jest kontyuowanie w prawym poddrzewie
            else: # jeżeli szukana wartość jest mniejsza od wartości węzła to wyzukiwanie jest kontynuowanie w lewym poddrzewie
                return self.wyszukiwanie(wezel.lewa, wartosc, wezel)

    def minimum(self, wezel): # Wyszukiwanie najmniejszego elementu
        minimum = wezel
        if wezel.lewa: # jeżeli istnieje lewe dziekco
            minimum = self.minimum(wezel.lewa) # rekurencyjnie znajdowana jest minimalna wartość w lewym poddrzewie
        return minimum

    def maksimum(self, wezel): # Wyszukiwanie największego elementu
        maksimum = wezel
        if wezel.prawa: # rekurencyjnie znajdowana jest największa wartość w prawym poddrzewie
            maksimum = self.maksimum(wezel.prawa)
        return maksimum

    def poprzednik(self, wezel): # Wyszukiwanie poprzednika
        if wezel.lewa:
            return self.maksimum(wezel.left)
        else:
            potencjalny = None
            aktualny = self.korzen
            while aktualny != wezel:
                if wezel.wartosc > aktualny.wartosc:
                    potencjalny = aktualny
                    aktualny = aktualny.prawa
                else:
                    aktualny = aktualny.lewa
            return potencjalny

    def nastepnik(self, wezel):
        if wezel.prawa:
            return self.minimum(wezel.prawa)
        else:
            potencjalny = None
            aktualny = self.korzen
            while aktualny is not wezel:
                if wezel.wartosc < aktualny.wartosc:
                    potencjalny = aktualny
                    aktualny = aktualny.lewa
                else:
                    aktualny = aktualny.prawa
            return potencjalny