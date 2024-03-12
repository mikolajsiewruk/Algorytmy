import random as rnd

def random_array(min, max, size):
    ciag = []
    for i in range(size):
        ciag.append(rnd.randint(min, max))
    return ciag

ciag = random_array(0,10,5)
print(ciag)
def bubble_sort(sort):
    print(sort)
    a = 1
    while a != 0:
        a = 0
        for i in range(len(sort)-1):
            if sort[i] > sort[i+1]:
                sort[i], sort[i+1] = sort[i+1], sort[i]
                a+=1
    return sort

print(bubble_sort(ciag))
def insertion_sort(sort):
    print(sort)
    for i in range(1, len(sort)):
        # check to ten element części nieposortowanej, który będziemy porównywali
        # z elementami części posortowanej
        check = sort[i]

        # ind_sorted to index aktualnie porównywanego elementu częsci posortowanej
        # na początku jest to element 0
        ind_sorted = i-1

        # przechodzimy przez elementy 'na lewo' od elementu sprawdzanego, tak długo jak są od niego większe
        # i pozostają jakieś niesprawdzone elementy 'na lewo' od niego
        while ind_sorted>=0 and check < sort[ind_sorted]:

            # trafiając na element większy przenosimy go o jedno miejsce 'w prawo' naszego ciągu
            sort[ind_sorted + 1] = sort[ind_sorted]

            # i przesuwamy się o kolejny element w lewo części 'sprawdzonej'
            ind_sorted -= 1

        # jeśli nasz sprawdzany element trafi na element mniejszy od siebie, ustawia się zaraz po nim
        sort[ind_sorted + 1] = check

    return sort
print(insertion_sort(ciag))