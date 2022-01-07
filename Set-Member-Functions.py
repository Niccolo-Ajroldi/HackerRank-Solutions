# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:32:11 2022

@author: nicco
"""

n = int(input())
s = set(map(int, input().split()))

n_cmnds = int(input())

for _ in range(n_cmnds):
    cmnd = input().split(" ")
    if cmnd[0] == "pop":
        s.pop()
    elif cmnd[0] == "discard":
        s.discard(int(cmnd[1]))
    elif cmnd[0] == "remove":
        s.remove(int(cmnd[1]))

print(sum(s))


