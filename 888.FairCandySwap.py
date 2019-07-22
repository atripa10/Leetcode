class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()
        s_a = sum(A)
        s_b = sum(B)
        i,j = 0,0
        while True:
            temp_a = s_a + B[i] - A[j]
            temp_b = s_b + A[j] - B[i]
            if temp_a == temp_b:
                return [A[j],B[i]]
            elif temp_a > temp_b:
                j += 1
            else:
                i += 1
                
