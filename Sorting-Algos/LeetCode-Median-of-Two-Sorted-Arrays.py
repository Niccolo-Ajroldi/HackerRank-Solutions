
# This solution is UGLY, but avoids to store the resulting sorted arrays
# Memory: O(1)
# Time: O(n/2)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        
        i = 0
        j = 0
        
        # tengo traccia degli ultimi due numeri
        if n1>0 and n2>0:
            x1 = min(nums1[0],nums2[0])
        elif n1>0 and n2==0:
            x1 = nums1[0]
        elif n1==0 and n2>0:
            x1 = nums2[0]
        x2 = x1
        
        while i<n1 and j<n2:
            if nums1[i] < nums2[j]:
                if i+j>0:
                    x1 = x2
                    x2 = nums1[i]
                i+=1
            else:
                if i+j>0:
                    x1 = x2
                    x2 = nums2[j]
                j+=1
                
            if (i+j)==n//2+1:
                break
        
        if (i+j)!=n//2+1:
            if i<n1:
                while (i+j)!=n//2+1:
                    x1 = x2
                    x2 = nums1[i]
                    i+=1
            elif j<n2:
                while (i+j)!=n//2+1:
                    x1 = x2
                    x2 = nums2[j]
                    j+=1
        
        # if n is even
        if (n%2==0):
            return float((x1+x2)/2)
        else:
            return x2

        