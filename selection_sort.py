#selection sort algorithm implementation in python 
def SelectionSort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i

        (l[start], l[minpos]) = (l[minpos], l[start])
    return l

l=[5,3,8,6,7,2,3]
print(SelectionSort(l))