# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:48:16 2022

@author: nicco
"""

import random as rand
import math

n = 20
a = 0; b=50;
v = [rand.randint(a,b) for _ in range(n)]
v = sorted(v)
v

def binary_search(v, val):
    n = len(v)
    l = 0
    r = n-1
    
    while l <= r:
        mid = int(math.floor((l+r)/2))
        if v[mid] == val:
            print("Found at position: %d", mid)
            return 1
        if val > v[mid]:
            l = mid+1
        else:
            r = mid-1
        
    return 0

v
binary_search(v,13)

