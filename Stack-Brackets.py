#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = deque()
    open_bracks = {"{", "[", "("} # set
    for _,c in enumerate(s):
        if c in open_bracks:
            stack.append(c)
        else:
            if len(stack)==0:
                return "NO"
            elif c=="}":
                if stack.pop()!="{":
                    return "NO"
            elif c=="]":
                if stack.pop()!="[":
                    return "NO"
            elif c==")":
                if stack.pop()!="(":
                    return "NO"
    
    if len(stack)!=0:
        if stack.pop() in open_bracks:
            return "NO"
            
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
