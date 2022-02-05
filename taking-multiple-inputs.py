# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:50:14 2022

@author: nicco
"""

n = int(input())

# returns a single string
input().strip() 

# returns a list of characters
input().split()

# returns a list of int
list(map(int, input().split()))


a = [print(a) for a in [1,2,4]]

a = [1,2,3]
str(a)

map(str, a)

list(map(str, a))

" ".join([str(el) for el in a])

" ".join(list(map(str,a)))
