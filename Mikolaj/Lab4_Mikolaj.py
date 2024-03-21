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

print(counting_sort([3,2,10,1,11,13]))