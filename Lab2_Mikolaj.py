from random import randint
def array_maker():
    arrays=[]
    for i in range(0,5):
        a=[]
        for i in range (0,6):
            r=randint(0,100)
            a.append(r)
        arrays.append(a)
    return arrays
ars=array_maker()
def bubble_sort(arr):
    changes=1
    i=0
    while changes!= 0:
        changes = 0
        for j in range (0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                changes+=1
    return arr
#print(bubble_sort(tab))
def insertion_sort(arr):
    for j in range(1,len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and key< arr[i]:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key
    return arr
def selection_sort(arr):
    for j in range (0,len(arr)):
        top = 0
        for i in range (0,len(arr)-j):
            if arr[i]>top:
                top=arr[i]
        arr[arr.index(top)],arr[-1-j]=arr[-1-j],arr[arr.index(top)]
    return arr
#print(selection_sort(tab))
for arr in ars:
    print(bubble_sort(arr))