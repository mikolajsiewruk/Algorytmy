import random as rnd
import time as tm
import matplotlib.pyplot as plt


def merge_sort(wektor):
    if len(wektor)>1:
        srodek=(len(wektor) // 2) #dzielenie wektoru na 2 równe części, lewą i prawą
        lewa = wektor[:srodek]
        prawa = wektor[srodek:]
        merge_sort(lewa)
        merge_sort(prawa)

        i=j=k=0 # początkowe indeksy podtablic

        while i < len(lewa) and j < len(prawa):
            if lewa[i] < prawa[j]: # jezeli element na pozycji i (lewa część) jest mniejszy od el na pozycji j (prawa część)
                wektor[k] = lewa[i] # umieszczamy go w wektorze k na pozycji i
                i += 1 # zwiększamy indeks tablicy
            else:
                wektor[k] = prawa[j] # jeżeli element na pozycji j jest mniejszy, to umieszczamy go w wektorze k na pozycji j
                j += 1
            k += 1 # zwiększamy indeks tablicy docelowej

        # scalanie części lewej i prawej
        while i < len(lewa):
            wektor[k] = lewa[i]
            i += 1
            k += 1

        while j < len(prawa):
            wektor[k] = prawa[j]
            j += 1
            k += 1
    return wektor

def counting_sort(wektor):
    maks=max(wektor)
    mini=min(wektor)
    posort=[] #posorotwane
    k=[0]*(maks+1) # lista zer, jej długość jest ustalana na podstawie maksymalnej wartości w wektorze zwiększonej o 1
    for i in range(len(wektor)): #przechodzenie przez całą długość wektora
        k[wektor[i]]= k[wektor[i]] + 1 # dla każdego elementu wektora i zwiększamy o jednen liczbę zer
    for j in range(len(k)): # przechodzimy przez listę zer
        if k[j]!=0: # jeżeli element j jest różny od 0, to dodajemy go do posortowanej części
            posort.append(j)
    return posort

def quick_sort(wektor): #zaczęte
    if len(wektor)>1:
        a = wektor[-2]
        l = 0
        p = len(wektor) - 1
        while l<p:
            print(a)
            print(wektor)
            print(l,p)
            if wektor[l]>a and wektor[p]<a:
                wektor[l],wektor[p] = wektor[p],wektor[l]
                p-=1
                l+=1

wektor=[5,4,2,100,9,250]
posortowany_wektor=counting_sort(wektor)
print(posortowany_wektor)


# rozmiary = [50, 100, 200, 500, 1000, 2000]
# for i in range(0, len(rozmiary)):
#     temporary = [rnd.randint(0, 5000) for _ in range(0, rozmiary[i])]
#     merge_sort.append(temporary.copy())
