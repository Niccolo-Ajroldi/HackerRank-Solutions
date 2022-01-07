# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:54:52 2022

@author: nicco
"""

row_1 = input().split(" "); n, m = [int(val) for val in row_1]
vec = input().split(" ")
A = input().split(" ")
B = input().split(" ")

A_set = set(A)
B_set = set(B)


# loop over v
h = 0
for val in vec:
    if val in A_set:
        h+=1
    if val in B_set:
        h-=1

print(h)

