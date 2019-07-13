class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        i = 0
        j = 0
        length = len(nums1)
        while i < m:
            if nums1[i] > nums2[0]:
                nums1[i],nums2[0] = nums2[0],nums1[i]
                nums2 = sorted(nums2)
            i+=1
        for l,k in enumerate(range(i,length)):
            nums1[k] = nums2[l]
