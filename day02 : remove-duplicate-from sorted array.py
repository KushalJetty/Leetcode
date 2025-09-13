class Solution(object):
    # Longest common prefix
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_values = list(set(nums))
        unique_values.sort()
        for u in range(len(unique_values)):
            nums[u] = unique_values[u]
        
        return len(unique_values)


strs = ["flower","flow","flight"]
lcp = Solution()
lcp.longestCommonPrefix()
