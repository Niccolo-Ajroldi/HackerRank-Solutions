# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:59:53 2022

@author: nicco
"""
if __name__ == '__main__':
    N = int(input())
    
    l = list() # or []
    
    for _ in range(N):
        cmnd = input().split(" ")
        
        if cmnd[0] == "insert":
            l.insert(int(cmnd[1]), int(cmnd[2]))
        elif cmnd[0] == "print":
            print(l)
        elif cmnd[0] == "remove":
            l.remove(int(cmnd[1]))
        elif cmnd[0] == "append":
            l.append(int(cmnd[1]))
        elif cmnd[0] == "sort":
            l.sort()
        elif cmnd[0] == "pop":
            l.pop()
        elif cmnd[0] == "reverse":
            l.reverse()
    #print(l)