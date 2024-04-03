import random
def generate():
    merge_arrays = []
    counting_arrays = []
    quicksort_arrays = []

    temporary = [random.randint(0, 5000) for _ in range(0, 5000)]
    merge_arrays.append(temporary.copy())
    counting_arrays.append(temporary.copy())
    quicksort_arrays.append(temporary.copy())
    return merge_arrays, counting_arrays, quicksort_arrays

def merge_sort(arr): # O(n*log(n))
    if len(arr) > 1:
        mid = int(len(arr) // 2)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
def counting_sort(arr): # O(n+k) gdzie n to liczba wyrazów tablicy a k to zakres
    top = max(arr)
    new = []
    zeros = [0] * (top + 1)
    for i in range(len(arr)):
        zeros[arr[i]] = zeros[arr[i]] + 1
    for j in range(len(zeros)):
        if zeros[j] != 0:
            new.append(j)
    return new
def quicksort(arr): # złożoność obliczeniowa O(n*log(n)), najgorszy przypadek O(n^2) kiedy pivot jest duży i powoduje niezbalansowany rozkład na strony
    if len(arr) >= 2:
        pivot = arr[len(arr)//2]
        print(pivot)
        l = 0
        r = len(arr) - 1
        while l < r:
            if arr[l] > pivot and arr[r] < pivot:
                arr[l], arr[r] = arr[r], arr[l]
            elif arr[l] == pivot and arr[r] < pivot:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
            elif arr[r] == pivot and arr[l] > pivot:
                arr[l], arr[r] = arr[r], arr[l]
                r -= 1
            elif arr[l] >= pivot:
                r -= 1
            elif arr[r] <= pivot:
                l += 1
            else:
                l += 1
                r -= 1
        c = arr.count(pivot)
        print("count", c)
        pvs=[x for x in arr if x == pivot]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        print(left,right)

        a = quicksort(left)
        b = quicksort(right)
        arr = a +pvs+ b
    return arr

m,c,q=generate()

print(m)
print(merge_sort(m[0]))

print(c)
print(counting_sort(c[0]))

print(q)
print(quicksort(q[0]))
