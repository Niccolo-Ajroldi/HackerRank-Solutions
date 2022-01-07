# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:12:41 2022

@author: nicco
"""

M = int(input())
A = [int(val) for val in input().split(" ")]
N = int(input())
B = [int(val) for val in input().split(" ")]

a_set = set(A)
b_set = set(B)

diff_1 = a_set.difference(b_set)
diff_2 = b_set.difference(a_set)

symm_diff = diff_1.copy()
symm_diff.update(diff_2)
symm_diff_list = sorted(symm_diff)

[print(val, end="\n") for val in symm_diff_list]
[print(val) for val in symm_diff_list]

