# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:26:44 2022

@author: nicco
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# def to_base_2(n):
#     n_2 = []
#     while n:
#         r = n % 2
#         if r:
#             n_2.append(1)
#         else:
#             n_2.append(0)
#         n = n//2
#     return n_2

def to_base_2(n):
    n_2 = []
    while n:
        n_2.append(n%2)
        n = n//2
    return n_2

def f(n_2):
    max_count = 0
    count = 0
    for i in n_2:
        if i == 1:
            count+=1
            max_count = max(count, max_count)
        else:
            count = 0
    return max_count

if __name__ == '__main__':
    n = int(input().strip())
    
    n_2 = to_base_2(n)
    
    print(n_2)
    print(f(n_2))
    
