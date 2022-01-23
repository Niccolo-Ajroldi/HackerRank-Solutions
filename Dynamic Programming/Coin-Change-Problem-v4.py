# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:48:25 2022

@author: nicco
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:55:06 2022
@author: nicco

    This version uses a binary tree, where I keep track of solution of subproblems,
    in order to avoid useless exploration of some subtrees already explored.
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
    # c = sorted(c)
    
    # empty dictionary, which stores keys (n,j) and correspondent value of the subproblem
    memo = {}
    
    return f_recursive(c, n,  memo)

# returns no. of ways to make up amount n with coins[0, ..., j]
def f_recursive(coins, n, memo):
    
    # key for memo
    key = (n,len(coins))
    
    if n == 0:
        return 1
    if n < 0:
        return 0
    if len(coins) == 0 and n > 0:
        return 0
    if key in memo:
        return memo[key]
    
    # first recursive call uses coins[-1], thus remove it from n
    # second recursiv call does not use coins[-1], thus n remains unchnaged, but coins[-1] is excluded from coins
    res = f_recursive(coins, n-coins[-1], memo) + f_recursive(coins[:-1], n, memo)
    memo[key] = res
    return res
    

n = 166 
m = 23
c = [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28]

n = 4 
m = 3
c = [1,2,3]

ways = getWays(n, c)
print(ways)












