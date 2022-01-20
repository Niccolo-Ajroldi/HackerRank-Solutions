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

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    if(n==1):
        print(arr)
        return
    
    val = arr[-1] # = arr[n-1]

    for i in range(n-2,-1,-1):
        if arr[i] < val:
            arr[i+1] = val
            print(" ".join([str(v) for v in arr]))
            return
        
        # shift arr[i] one cell to the right
        arr[i+1] = arr[i]
        print(" ".join([str(v) for v in arr]))
    
    if i==0: # can be commented out
        arr[i] = val
        print(" ".join([str(v) for v in arr]))
    
    return
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
