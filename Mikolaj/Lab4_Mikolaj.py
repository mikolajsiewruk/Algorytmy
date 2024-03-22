import random
l=[]
for i in range(0,50):
    l.append(random.randint(0,1000))
def merge_sort(arr):
    if len(arr)>1:
        mid=int(len(arr)//2)
        L=arr[:mid]
        R=arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def counting_sort(arr):
    top=max(arr)
    low=min(arr)
    new=[]
    zeros=[0]*(top+1)
    for i in range(len(arr)):
        zeros[arr[i]]=zeros[arr[i]]+1
    for j in range(len(zeros)):
        if zeros[j]!=0:
            new.append(j)
    return new

def quicksort(arr):
    if len(arr)>2:
        pivot=arr[-2]
        l=0
        r=len(arr)-1
        while l<r:
            print(pivot)
            print(arr)
            print(l,r)
            if arr[l]>pivot and arr[r]<pivot:
                arr[l],arr[r]=arr[r],arr[l]
            elif arr[l]==pivot and arr[r]<pivot:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
            elif arr[r] == pivot and arr[l] > pivot:
                arr[l], arr[r] = arr[r], arr[l]
                r-=1
            elif arr[l]>=pivot:
                r-=1
            elif arr[r]<=pivot:
                l+=1
            else:
                l += 1
                r -= 1
        c=arr.count(pivot)
        left = arr[:arr.index(pivot)]
        right = arr[arr.index(pivot):]
        if not left or not right:
            arr = left+right
        print(left)
        print(right)
        a=quicksort(left)
        b=quicksort(right)
        arr=a+b
    return arr
print(quicksort(l))