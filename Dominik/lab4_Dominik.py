def split(to_split):
    if len(to_split) <=1:
        return to_split
    else:
        mid=int(len(to_split) / 2)
        a1= to_split[0:mid]
        a2= to_split[mid:]
        print(a1 + a2)
        return split(a1) + split(a2)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    merged.extend(left[i:])
    merged.extend(right[j:])
    print(merged)
    return merged

def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    splited = split(unsorted)
    return merge(merge_sort(splited[:len(splited)//2]), merge_sort(splited[len(splited)//2:]))


x = [1,2,3,10,4,5,6,9,0,5,6,7,8,7,65,4,4,333,22,3]
print(merge_sort(x))
