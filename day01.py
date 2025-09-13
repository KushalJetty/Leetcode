# two sum problem

class Solution(object):
    # Two Sum
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                sum = 0
                if not i == j:
                    # print(nums[i] , nums[j])
                    sum = nums[i] + nums[j]
                if sum == target:
                    print([i, j])
                    break
                    # return [nums.index(i), nums.index(j)]
        print("hii")
        return 0

nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6

s= Solution()
s.twoSum(nums1,target1)
s.twoSum(nums2,target2)
s.twoSum(nums3 ,target3)

# length of the last word

class Solution(object):
    # Length of the last word
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.a = s.split()
        return int(len(self.a[-1]))
    
# 28. Find the Index of the First Occurrence in a String
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return int(haystack.index(needle))
        else:
            return -1
        
needle = "sad"
haystack = "sadbutsad"

a = "   fly me   to   the moon  "
res = Solution()

print(f"{res.lengthOfLastWord(a)}")