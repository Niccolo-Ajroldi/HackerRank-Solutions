# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:32:23 2022

@author: nicco
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    
    # iterate from second value to the last
    # this is done because the first element has no predecessors 
    for i in range(1,n):
        
        # save value, because arr[i] will change, it will contain
        # shifts of arr[i-1] if arr[i-1]>arr[i]
        value = arr[i]
        
        # iterate over predecessors of arr[i]
        for j in range(i-1,-2,-1):
            
            # If I have not found a predecessor smaller than value, 
            # I put value at the start of the array
            if j==-1:
                arr[0] = value
                
            # If value is greater than arr[j],
            # then the assignment places value after arr[j]
            # In the case j==(i-1) the assignment is useless
            elif arr[j] < value:
                arr[j+1] = value
                break
            
            # If the value is less than arr[j], 
            # then propagate arr[j] one step ahed
            # This is done because we "free" a space before arr[j],
            # that we might fill with value
            elif arr[j] > value:
                arr[j+1] = arr[j]
            
        print(" ".join([str(v) for v in arr]))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
