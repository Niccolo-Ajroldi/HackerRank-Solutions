# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:12:52 2022

@author: nicco
"""


n = int(input())
arr = list(map(int,input().split()))

def partition(arr):
    
    pivot = arr[0]
    
    left  = []
    right = []
    equal = [pivot]
    
    for el in arr[1:]:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)      
    
    return left, equal, right

def quicksort(arr):
    
    # if arr is empty
    if not arr:
        return []
    
    left, equal, right = partition(arr)
    
    if len(left) > 1:
        left  = quicksort(left)
        
    if len(right) > 1:
        right  = quicksort(right)
    
    res = left + equal + right
    
    print(" ".join(map(str,res)))
    return res

quicksort(arr)
