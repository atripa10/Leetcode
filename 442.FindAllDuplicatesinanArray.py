class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(N) space and time
        # dict = {}
        # ans = set()
        # for i in nums:
        #     if i in dict:
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1
        # for i in range(len(nums)):            
        #     if dict[nums[i]] == 2:
        #         ans.add(nums[i])
        # return list(ans)
       #### O(1) space , O(N) time #####
        ans = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                ans.append(abs(n))
        return ans
        
