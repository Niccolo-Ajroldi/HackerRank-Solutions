# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:31:04 2022

@author: nicco
"""

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    
    if len(w)==1:
        return "no answer"

    w_list = list(map(str,w))
    res_list = w_list
    flag = False
    
    for i in range(len(w_list)-2,-1,-1):
        if w_list[i] < w_list[i+1]:
            
            # considero w[i:]
            temp = sorted(w_list[i:])
            
            print(temp,w_list[i])
            # cerco il primo numero maggiore di w[i]
            idx = next(j for j,c in enumerate(temp) if c > w_list[i])
            
            # il primo numero maggiore di w[i] va all'inizio
            res_list[i] = temp[idx]
            
            # gli altri seguono in ordine crescente
            res_list[(i+1):] = temp[:idx] + temp[idx+1:]
            
            flag = True
            break
    
    if flag:
        return "".join(map(str,res_list))
    else:
        return "no answer"

w = "dkhc"    
biggerIsGreater(w)

temp = sorted(w)
temp
"".join(temp[1:])

next(i for i,c in enumerate(temp) if c>w_list[0])


