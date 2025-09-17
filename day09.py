class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for index,num in enumerate(nums1):
            if num == 0 and i<n:
                nums1[index] = nums2[i]
                i = i+1
            else:
                continue
        nums1.sort()
        return nums1