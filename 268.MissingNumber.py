class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         #O(N) space O(N) time
#         dict = {}
#         for n in nums:
#             dict[n] = 1
        
#         for i in range(0,len(nums)+1):
#             if i not in dict:
#                 return i

        #O(1) space
        l = len(nums)
        sum_to_n_terms = l*(l+1)/2
        sum_of_numbers_in_list = sum(nums)
        return sum_to_n_terms - sum_of_numbers_in_list
