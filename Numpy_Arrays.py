#You are given a space separated list of numbers.
#Your task is to print a reversed NumPy array with the element type float.

import numpy

def arrays(arr):
    x=arr[::-1]
    b = numpy.array(x,float)
    return b
        
        

arr = input().strip().split(' ')
result = arrays(arr)
print(result)