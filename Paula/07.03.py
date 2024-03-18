import random as rnd
def losowanie(N,min_w, max_w):
    return [rnd.randint (min_w, max_w) for i in range(N)]
N = 5
min_w = 0
max_w = 10
wektor = losowanie(N, min_w, max_w)
print("Wygenerowany wektor:", wektor)

def sortowanie_babelkowe(wektor):
    n = len(wektor)
    for i in range(n):
        for j in range(len(wektor) - 1 - i):
            if wektor[j] > wektor[j + 1]:
                wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
    return wektor
print('Sortowanie bąbelkowe:',sortowanie_babelkowe(wektor))

def insertion(wektor):
    for i in range(1, len(wektor)):
        j = i - 1
        while j >= 0 and wektor[j] > wektor[j + 1]:
            wektor[j], wektor[j + 1] = wektor[j + 1], wektor[j]
            j -= 1
    return wektor
print('Sortowanie przez wstawianie:',insertion(wektor))

def selection(wektor):
    for i in range(len(wektor)):
        min_i= i
        for j in range(i, len(wektor)):
            if wektor[min_i] > wektor[j]:
                min_w = j
        wektor[min_i], wektor[i] = wektor[i], wektor[min_i]
    return wektor
print('Sortowanie przez wybieranie:',selection(wektor))





















