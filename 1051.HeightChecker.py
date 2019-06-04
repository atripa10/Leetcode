class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sortedHeights = sorted(heights)
        print sortedHeights
        count = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                count+=1
        return count
