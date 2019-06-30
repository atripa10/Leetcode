class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #Linear Solution 
        
        # for i in range(len(A)-1):
        #     if A[i] > A[i+1]:
        #         return i
        # # binary search
        
        lo, hi = 0, len(A) -1
        while lo < hi:
            middle = (lo + hi) /2
            if A[middle] < A[middle+1]:
                lo = middle +1
            else:
                hi = middle
        return lo
