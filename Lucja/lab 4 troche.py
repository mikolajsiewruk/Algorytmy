import random as rnd


def merge_sort(tablica):
    if len (tablica)>1: #jesli dlugosc tablicy wieksza niz jeden
        srodek=len(tablica)//2 #to podziel na 2
        prawa=tablica[srodek:]
        lewa=tablica[:srodek]
        merge_sort(lewa)
        merge_sort(prawa)
        p=0
        t=0
        l=0
    while l < len(lewa) and p < len(prawa):
        if lewa[l]<prawa[p]:
            tablica[t]=lewa[l]
            l=l+1 #zwiekszenie indeksu
        else:
            tablica[t]=prawa[p]
            p=l+1
            t=t+1
    while l<len (lewa):
        tablica[t]=lewa[l]
        l=l+1
        t=t+1
    while p<len(prawa):
        tablica[t]=prawa[p]
        l=l+1
        t=t+1
    return tablica


def counting_sort(tablica):
    gora = max(tablica) #wart min max
    dol= min(tablica)
    y = [] #lista na posortowane argumeny
    k = [0]*(gora+1) #tablica k o długości ymax - ymin + 1 zawierającą same wartości 0
    for i in range(len(tablica)):
        k[tablica[i]]=k[tablica[i]]+1 #iteruj po każdym elemencie yi z listy y i zwiększ o 1 wartość listy k w indeksie yi − ymin
    for j in range(len(k)):
        if k[j]!=0: #dodaje indeks do listy wyjsciowej jesli nie jest on rowny 0
            y.append(j)
    return y
