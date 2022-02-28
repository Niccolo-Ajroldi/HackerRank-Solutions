# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:48:30 2022

@author: nicco
"""

# SBAGLIATO!!
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        
        i = 0
        j = 0
        # tengo traccia degli ultimi due numeri
        x1 = min(nums1[0], nums2[0])
        x2 = max(nums1[0], nums2[0])
        count = 0
        while i+j != (n//2):
            
            if i<=n1-1 and j<=n2-1:
                if nums1[i] < nums2[j]:
                    x1 = x2
                    x2 = nums1[i]
                    i += 1
                else:
                    x1 = x2
                    x2 = nums2[j]
                    j += 1
            elif i>n1-1:
                    j += 1
                    x1 = x2
                    x2 = nums2[j]
            elif j>n2-1:
                    i += 1
                    x1 = x2
                    x2 = nums1[i]
                
        # if n is even
        if (n%2==0):
            return float((x1+x2)/2)
        else:
            return x1

        