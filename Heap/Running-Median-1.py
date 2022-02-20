# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 18:11:25 2022

@author: nicco
"""

exec(open(r"D:\Coding\HackerRank-Solutions\Heap\heap_src.py").read())


# input
v_in = [12, 4, 5, 3, 8, 7]
v_in = [10,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10]
print(v_in)

# max heap
maxh = MaxHeap(1000)
minh = MinHeap(1000)

median = None

#
for el in v_in:
    
    if not median:
        maxh.insert(el)
        median = el
        
    else:
        
        # insert el in one heap
        if el < median:
            print("inserting %d in maxheap" %el)
            maxh.insert(el)
        else:
            print("inserting %d in minheap" %el)
            minh.insert(el)
                
        # restore balancing balancing between heaps
        if maxh.size - minh.size > 1:
            print("moving %d to minheap" %maxh.get_max())
            minh.insert(maxh.pop_max())
        elif minh.size - maxh.size > 1:
            print("moving %d to maxheap" %minh.get_min())
            maxh.insert(minh.pop_min())
        # if el==3:
        #     break
        
        if maxh.size == minh.size:
            median = (minh.get_min() + maxh.get_max())/2
        elif maxh.size == minh.size + 1:
            median = maxh.get_max()
        elif minh.size == maxh.size + 1:
            median = minh.get_min()
        
    print(median)
    
maxh.print()
minh.print()


a = 1
if True:
    a=2
a


