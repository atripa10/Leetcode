class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])
        for i,n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans
