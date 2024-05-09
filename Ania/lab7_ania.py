from tabulate import tabulate
import pandas as pd

class HuffmanTreeNode:
    def __init__(self, wartosc, litera):
        self.value = wartosc
        self.lewa = None
        self.prawa = None
        self.litera = litera

class Kompresja:

    def kompresja_huffmana(self, tekst: str) -> HuffmanTreeNode:

        def keys(item):
            return item[1]

        znaki_specjalne = []
        dictionary = {}
        for litery in tekst:  # dodanie wszystkich znaków do listy bez powtórzeń
            if litery not in znaki_specjalne:
                znaki_specjalne.append(litery)
        for litery in znaki_specjalne:  # następuje tworzenie słownika, gdzie kay jest literą, a wartość ilością jej powtórzeń
            dictionary[litery] = tekst.count(litery)
        dictionary_desc = dict(sorted(dictionary.items(), key=lambda item: -item[1]))  # sortowanie słownika
        items = []
        i = dictionary_desc.items()
        for item in i:  # dodanie elementów w słowniku do listy
            items.append([item[0], item[1]])

        items.sort(key=lambda item:item[1], reverse=True)  # sortowanie listy na podstawie ilości wystąpień

        while len(items) > 1:  # algorytm kompresji Huffmana
            i1 = items[-1]
            i2 = items[-2]
            if len(i1) == 2 and len(i2) == 2:  # jeżeli oba elementy nie są reprezentowane przez żaden węzeł
                korzen = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])  # tworzenie węzła sumującego
                korzen.lewa = HuffmanTreeNode(i1[1], i1[0])  # dodawanie liści
                korzen.prawa = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))  # usuwanie liter z listy
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                wartosc = i1[1] + i2[1]
                items.append([t, wartosc, korzen])  # w ich miejsce dodawany jest element reprezentujący obie litery
                items.sort(key=lambda item:item[1], reverse=True)
            elif len(i1) == 2 and len(i2) != 2:  # jeżeli prawy element jest węzłem, a lewy nie
                korzen = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                korzen.lewa = HuffmanTreeNode(i1[1], i1[0])
                korzen.prawa = i2[2]
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                wartosc = i1[1] + i2[1]
                items.append([t, wartosc, korzen])
                items.sort(key=lambda item:item[1], reverse=True)
            elif len(i1) != 2 and len(i2) == 2:  # jeżeli lewy jest węzłem, a prawy nie
                korzen = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                korzen.lewa = i1[2]
                korzen.prawa = HuffmanTreeNode(i2[1], i2[0])
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                wartosc = i1[1] + i2[1]
                items.append([t, wartosc, korzen])
                items.sort(key=lambda item:item[1], reverse=True)
            else:  # jeżeli oba elementy są węzłami
                korzen = HuffmanTreeNode(i1[1] + i2[1], i1[0] + i2[0])
                korzen.lewa = i1[2]
                korzen.prawa = i2[2]
                items.pop(items.index(i1))
                items.pop(items.index(i2))
                t = i1[0] + i2[0]
                wartosc = i1[1] + i2[1]
                items.append([t, wartosc, korzen])
                items.sort(key=lambda item:item[1], reverse=True)

        return items[0][2]  # zwracany jest korzen drzewa

    def zliczanie(self, tekst: str, litera: str):
        znaki_specjalne = []
        slownik = {}
        for litery in tekst:
            if litery not in znaki_specjalne:
                znaki_specjalne.append(litery)
        for litery in znaki_specjalne:
            slownik[litery] = tekst.count(litery)
        for key in slownik.keys():
            if litera == key:
                return slownik.get(key)
        return print("Taka litera nie istnieje")

    def kodowanie(self, wezel: HuffmanTreeNode, litera: str, kod: str) -> str:
        if wezel:
            if litera == wezel.litera:
                return kod
            if litera in wezel.lewa.litera:
                kod += "0"
                return self.kodowanie(wezel.lewa, litera, kod)
            else:
                kod += "1"
                return self.kodowanie(wezel.prawa, litera, kod)
        else:
            return kod

    def dekodowanie(self, wezel: HuffmanTreeNode, kod: str) -> str:
        if len(kod) == 0:
            return wezel.litera
        if kod[0] == '0':
            return self.dekodowanie(wezel.lewa, kod[1:])
        else:
            return self.dekodowanie(wezel.prawa, kod[1:])

    def bit(self, wezel: HuffmanTreeNode, tekst: str): # zliczanie liczby bitów przed i po kompresji
        bit_poczatkowe = len(tekst) * 8
        bit_Huffman = 0
        znaki_specjalne = []
        for litery in tekst:
            if litery not in znaki_specjalne:
                znaki_specjalne.append(litery)
        for znak in znaki_specjalne:
            kod = self.kodowanie(wezel, znak, "")
            bit_Huffman += len(kod)

        return bit_poczatkowe, bit_Huffman

    def znaki(self, wezel: HuffmanTreeNode, tekst:str):
        znaki_specjalne = []
        tab = []
        for litery in tekst:
            if litery not in znaki_specjalne:
                znaki_specjalne.append(litery)
        for znak in znaki_specjalne:
            ilosc = self.zliczanie(tekst, znak)
            kod = self.kodowanie(wezel, znak, "")
            tab.append([znak, ilosc, kod])

        return print(tabulate(tab))

    def kodowanie_tekstu(self, wezel, text):
        tekst_binarny = ""
        for litera in text:
            kod = self.kodowanie(wezel, litera, "")
            kod = "".join(kod)
            tekst_binarny += kod
        return tekst_binarny

    def dekodowanie_tekstu(self, wezel, tekst):
        tekst_oryginalny = ""
        end = 0
        while len(tekst) > 0:
            znak = tekst[0:end]
            kodowanie = self.dekodowanie(wezel, znak)
            if len(kodowanie) == 1:
                tekst_oryginalny += kodowanie
                tekst = tekst[end:]
                end = 0
            else:
                end = end + 1
        return tekst_oryginalny


k = Kompresja()
w_1 = open("w_1.txt")
w_1 = w_1.read()
w1 = k.kompresja_huffmana(w_1)
w_3 = open("w_3.txt")
w_3 = w_3.read()
w3 = k.kompresja_huffmana(w_3)
w_10 = open("w_10.txt")
w_10 = w_10.read()
w10 = k.kompresja_huffmana(w_10)
w_25 = open("w_25.txt")
w_25 = w_25.read()
w25 = k.kompresja_huffmana(w_25)
w_50 = open("w_50.txt")
w_50 = w_50.read()
w50 = k.kompresja_huffmana(w_50)


z1 = k.znaki(w1, w_1)
z3 = k.znaki(w3, w_3)
z10 = k.znaki(w10, w_10)
z25 = k.znaki(w25, w_25)
z50 = k.znaki(w50, w_50)

kod1 = k.kodowanie_tekstu(w1, w_1)
print(k.dekodowanie_tekstu(w1, kod1))




