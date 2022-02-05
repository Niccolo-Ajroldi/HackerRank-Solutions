# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:39:19 2022

@author: nicco
"""

# n = int(input())
# arr = list(map(int, input().split()))

n = 7
arr = [1, 3, 9, 8, 2, 7, 5]

# partition [start, end)
def partition(arr, start, end):
    
    pivot = arr[end-1]
    p_idx = end-1
    
    # iterate over arr to be splitted
    i = start
    while i != p_idx:
        #print(i, arr)
        if arr[i] < pivot:
            i+=1
            continue
        if arr[i] > pivot:
            # swap arr[i] and arr[p_idx-1], notice that if i==p_idx-1 this swap is useless but harmless
            arr[i], arr[p_idx-1] = arr[p_idx-1], arr[i]
            # swap arr[p_idx-1], arr[p_idx]
            arr[p_idx-1], arr[p_idx] = arr[p_idx], arr[p_idx-1]
            #arr[i], arr[p_idx-1], arr[p_idx] = arr[p_idx-1], arr[p_idx], arr[i]
            p_idx = p_idx - 1
    
    print(" ".join(map(str,arr)))
    return p_idx


def quicksort_rec(arr, start, end):
    
    if start == end:
        return
    
    # partition and get pivot index (p_idx)
    p_idx = partition(arr, start, end)
    
    if p_idx - start > 1:
        #print("calling quicksort_rec with start="+str(start)+", end="+str(p_idx))
        quicksort_rec(arr, start, p_idx)
        
    if end - p_idx - 1 > 1:
        #print("calling quicksort_rec with start="+str(p_idx+1)+", end="+str(end))
        quicksort_rec(arr, p_idx+1, end)
    
    
def quicksort_inplace(arr):
    quicksort_rec(arr, 0, len(arr))

arr = [1, 3, 9, 8, 2, 7, 5]
arr
quicksort_inplace(arr)
arr
