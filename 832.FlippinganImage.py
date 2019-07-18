class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for li in A:
            li.reverse()
            for i in range(len(li)):
                if li[i] == 1:
                    li[i] = 0
                else:
                    li[i] = 1
        return A
                
