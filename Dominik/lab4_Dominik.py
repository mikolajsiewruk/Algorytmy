

def split(to_split):
    if len(to_split) <=1:
        return to_split
    else:
        mid=int(len(to_split) / 2)
        a1= to_split[0:mid]
        a2= to_split[mid:]
        return split(a1), split(a2)

def count_items(nested_tuple):
    counter = 0
    for item in nested_tuple:
        if isinstance(item, str):
            counter += len(item)
        elif isinstance(item, tuple):
            counter += count_items(item)
    return counter

def merge(to_merge):
    new=[]
    if len(new) == count_items(to_merge):
        return new
    else:
        for i in range(0,len(to_merge)-1):
            for j in range(0,len(to_merge[i])-1):
                for k in range(0, to_merge[i][j]-1):
                    if to_merge[i][j][k]<to_merge[i+1][j]:
                        new.append(to_merge[i][j])
                        new.append(to_merge[i+1][j])
                    else:
                        new.append(to_merge[i+1][j])
                        new.append(to_merge[i][j])
        return merge(new)

a=([2,3], [3,7])
x = (split([1,2,3,10,4,5,6,9,0,5,6,7,8,7,65,4,4,333,22,3]))
print(x)
print(merge(a))