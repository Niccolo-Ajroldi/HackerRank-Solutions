# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:55:06 2022
@author: nicco

    This version uses a NON-BINARY tree.
    However, the tree is constructed in a samrt way in order to avoid
    finding multiple times the same solution.

    A major problem of this version is taht it does not save informarions about
    explored subtrees. Thus it becomes very slow.

    "This version has been improved in Coin-Change-Problem-v3-py""    
"""
#!/bin/python3


import math
import os
import random
import re
import sys
import numpy as np


#
# The function RETURNS a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    
    # O(m)
    c = sorted(c)
    
    return f_recursive(n, c)

def f_recursive(n, c):
    
    print(n, c)
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    if len(c) == 0 and n>0:
        return 0
        
    res = 0
    for i in range(len(c)):
        res += f_recursive(n-c[i], c[:(i+1)])
    return res


n = 4
m = 3
c = [1,2,3]

#n = 166 
#m = 23
#c = [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28]


ways = getWays(n, c)
print(ways)












