# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:25:05 2022

@author: nicco
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    
    # Timsort: O(nlogn) on average and worst, O(n) at best
    # O(n) in space
    arr_sort = sorted(arr)
    valid_pairs = []
    
    smallest_diff = arr_sort[-1] - arr_sort[0]
    n = len(arr_sort)
    
    for i in range(1,n):
        
        diff_i = arr_sort[i] - arr_sort[i-1]
        
        if  diff_i < smallest_diff:
            smallest_diff = diff_i
            valid_pairs = [arr_sort[i-1],arr_sort[i]]
            
        elif  diff_i == smallest_diff:
            smallest_diff = diff_i
            valid_pairs = valid_pairs + [arr_sort[i-1],arr_sort[i]]
    
    return valid_pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
