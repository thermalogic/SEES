
def select_sort(L):
    length=len(L)
    for i in range(length):
        min_idx = i 
        for j in range(i+1, length):
            if L[j]<L[min_idx] :
                min_idx = j
        if min_idx!=i:
            L[i], L[min_idx] = L[min_idx], L[i]   

def merge(left, right, compare = lambda x,y:x<y):
    result = []  # the copy of the list.
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare = lambda x,y:x<y):
    if len(L) < 2:
        return L[:] 
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)
