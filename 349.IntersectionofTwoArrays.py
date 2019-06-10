class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution 1
        dict1 = collections.Counter(nums1)
        dict2 = collections.Counter(nums2)
        return list((dict&dict2).elements())

        # solution 2
        #create 1st Dictionary
        dict1 = {}
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        #create 2nd Dictionary        
        ans = []
        for num in nums2:
            if num in dict1:
                ans.append(num)
        return set(ans)
