import random as rnd

ciag = []
for i in range(5):
    ciag.append(rnd.randint(0,10))

print(ciag)
def bubble_sort(sort):
    a = 1
    while a != 0:
        a = 0
        for i in range(len(sort)-1):
            if sort[i] > sort[i+1]:
                sort[i], sort[i+1] = sort[i+1], sort[i]
                a+=1
    return sort

#print(bubble_sort(ciag))

def insertion_sort(sort):
    sorted = [sort[0]]
    unsorted = sort[:1]
    while len(sorted) < len(sort):
        lalalala
    return sorted

print(insertion_sort(ciag))