tab=[10,12,1,8,9,4,100]
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
print(insertion_sort(tab))