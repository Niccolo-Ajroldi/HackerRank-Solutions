# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:59:29 2022

@author: nicco
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    dic = {}
    for word in magazine:
        if not word in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for word in note:
        if not word in dic:
            print("No")
            return
        if dic[word]==0:
            print("No")
            return
        dic[word] -= 1
    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

    print