# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:34:37 2022

@author: nicco
"""

# n = int(input())
# arr = list(map(int, input().split()))

n = 7
arr = [1, 3, 9, 8, 2, 7, 5]

# partition [start, end)
def partition(arr, start, end):
    
    pivot = arr[end-1]
    
    # iterate over arr to be splitted
    i = start
    
    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # reallocate the pivot
    arr[i], arr[end-1] = arr[end-1], arr[i]
    
    print(" ".join(map(str,arr)))
    return i

# arr = [1, 3, 9, 8, 2, 7, 5]
# partition(arr, 0, len(arr))
# arr

# arr = [1, 3, 9, 8, 2, 7, 5]
# partition(arr, 0, 5)
# arr

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
