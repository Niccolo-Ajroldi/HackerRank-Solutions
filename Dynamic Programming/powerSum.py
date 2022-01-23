# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:58:28 2022

@author: nicco
"""
#!/bin/python3

import math
import os
import random
import re
import sys

"""
Find the number of ways that a given integer, X, 
can be expressed as the sum of the N powers of unique, natural numbers.

For example, if X=13 and N=2, we have to find all combinations 
of unique squares adding up to 13. The only solution is 2^2 + 3^2.

Resursive-dynamic-programming-style solution:
    https://www.hackerrank.com/challenges/the-power-sum/forum/comments/278697
"""

# TODO: implement in a more efficient way, removing the highest element
# each time, instead of the smallest
# compelxity is in such case reduced because we do not have to reasssing available
# just use .pop()


def powerSum(X, N):
    
    # numero + grande che ha senso guardare:
    n_max = math.floor(X**(1/N))
    
    # O(floor(X**(1/n)))
    available = [i**N for i in range(1,n_max+1)]
    print(available)
    return f_rec(X, available)

# O(2^floor(X**(1/N)))
def f_rec(target, available):
    
    # se target è minore di zero non procedo oltre --> prune tree
    if target < 0:
        return 0 
    
    # se target è zero, sono in una foglia e la lista è vuota, 
    # oppure sono + sopra, e la lista non è vuota, in ogni caso return 1
    elif target == 0:
        return 1
    
    # se sono in una foglia e il target non è zero, return 0
    elif len(available)==0 and target !=0:
        return 0

    else:       
        smallest = available[0]
        available = available[1:len(available)]
        
        return f_rec(target-smallest, available) + f_rec(target, available)
    

X = 100 # int(input())
N = 2 # int(input())

powerSum(X, N)



# total complexity:   
#                   O(2^M), with M = X**(1/N)







