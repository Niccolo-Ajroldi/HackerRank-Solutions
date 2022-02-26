# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:53:50 2022

@author: nicco
"""

import math

versions = [1, 4, 45, 26, 16, 16, 16, 16, 16, 16, 16]
# versions = [16]*4
len(versions)
def is_bad(idx):
    return versions[idx]==16


def find_bad_revision(known_good: int, known_bad:int) -> int:
    
    while known_bad - known_good > 1:
        mid = int(math.floor((known_bad+known_good)/2))
        
        if is_bad(mid):
            known_bad = mid
        
        else:
            known_good = mid
            
    return known_bad
    
    
find_bad_revision(0,len(versions)-1)
