#insertion sort algorithm implementation in python
#insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time
#it is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort
#however, insertion sort provides several advantages:
#simple implementation, efficient for (quite) small data sets, more efficient in practice than most other simple quadratic (i.e., O(n^2)) algorithms such as selection sort or bubble sort


def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1

    return seq

seq = [5,3,8,6,7,2,3]
print(InsertionSort(seq))
