# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:55:40 2022

@author: nicco
"""
#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    
    words = string.ascii_lowercase
    
    w_h_dict = dict(zip(words,h))
    #w_h_dict = {k:v for k,v in zip(words, h)}
    
    max_height = 1
    for c in word:
        max_height = max(w_h_dict[c], max_height)
        
    w_length = len(word)
    
    return w_length*max_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
