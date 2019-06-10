class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = collections.Counter(nums1)
        dict2 = collections.Counter(nums2)
        return list((dict1&dict2).elements())
        '''
        answer = []
        for key in dict1:
            if key in dict2:
                reps = min(dict1[key],dict2[key])
                for i in range(0,reps):
                    answer.append(key)
        return answer
        '''
