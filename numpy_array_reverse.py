#nmpy array reverse
#You are given a space separated list of numbers.
#Your task is to print a reversed NumPy array with the element type float.
#Note
#A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.
#Example

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    #
    array = numpy.array(arr, dtype=float)
    
    return array[::-1]
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)