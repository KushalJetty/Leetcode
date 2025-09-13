class Solution(object):
    # 27.Remove Element
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i< len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            i = i+1
        k = len(nums)
        return k
        
nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
k = obj.removeElement(nums, val)
print(k, nums)

# original_list = ['a', 'b', 'c', 'd', 'e', 'f']
# indices_to_remove = [1, 3, 5]  # Indices of 'b', 'd', 'f'

# new_list = [element for index, element in enumerate(original_list) if index not in indices_to_remove]
# print(new_list)