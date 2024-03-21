import random as rnd
def losowanie(N, min_w, max_w):
    return [rnd.randint(min_w, max_w) for _ in range(N)]

def sortowanie_babelkowe(wektor):
    n = len(wektor)
    for i in range(n):
        for j in range(len(wektor) - 1 - i):
            if wektor[j] > wektor[j + 1]:
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
    return wektor

def insertion(wektor):
    for i in range(1, len(wektor)):
        j = i - 1
        while j >= 0 and wektor[j] > wektor[j + 1]:
            wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
            j -= 1
    return wektor

def selection(wektor):
    for i in range(len(wektor)):
        min_i = i
        for j in range(i, len(wektor)):
            if wektor[min_i] > wektor[j]:
                min_i = j
        wektor[min_i], wektor[i] = wektor[i], wektor[min_i]
    return wektor

def test_sortowania(N):
    min_w = 0
    max_w = 100

    for _ in range(N):
        wektor = losowanie(N, min_w, max_w)
        wektor_babelkowe = wektor.copy()
        wektor_wstawianie = wektor.copy()
        wektor_wybieranie = wektor.copy()

        print("WYGENEROWANY WEKTOR:", wektor)

        sortowanie_babelkowe(wektor_babelkowe)
        insertion(wektor_wstawianie)
        selection(wektor_wybieranie)

        print("Sortowanie bąbelkowe:", wektor_babelkowe)
        print("Sortowanie przez wstawianie:", wektor_wstawianie)
        print("Sortowanie przez wybieranie:", wektor_wybieranie)

N = int(input("Podaj liczbę N: "))
test_sortowania(N)
