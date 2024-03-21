import random as rnd
def losowanie(N,min_w, max_w):
    return [rnd.randint (min_w, max_w) for _ in range(N)]
N = 5
min_w = 0
max_w = 10
wektor1 = losowanie(N, min_w, max_w)
print("Wygenerowany wektor:", wektor1)

def sortowanie_babelkowe(wektor1):
    n = len(wektor1)
    for i in range(n):
        for j in range(len(wektor1) - 1 - i):
            if wektor1[j] > wektor1[j + 1]:
                wektor1[j], wektor1[j + 1] = wektor1[j + 1], wektor1[j]
    return wektor1
print('Sortowanie bąbelkowe:',sortowanie_babelkowe(wektor1))

def insertion(wektor1):
    for i in range(1, len(wektor1)):
        j = i - 1
        while j >= 0 and wektor1[j] > wektor1[j + 1]:
            wektor1[j], wektor1[j + 1] = wektor1[j + 1], wektor1[j]
            j -= 1
    return wektor1
print('Sortowanie przez wstawianie:',insertion(wektor1))

def selection(wektor1):
    for i in range(len(wektor1)):
        min_i= i
        for j in range(i, len(wektor1)):
            if wektor1[min_i] > wektor1[j]:
                min_i = j
        wektor1[min_i], wektor1[i] = wektor1[i], wektor1[min_i]
    return wektor1
print('Sortowanie przez wybieranie:',selection(wektor1))





















