class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for index, num in enumerate(nums):
                if num == target:
                    return index
        else:
            for index,num in enumerate(nums):
                if target < num:
                    return index
            return int(len(nums))
        
    def convert_to_num(self,l):
        res = 0
        l1 = []
        curentNode = l
        while curentNode:
            l1.append(curentNode.val)
            curentNode = curentNode.next
            
        for num in l1[::-1]:
            res = res*10 + num
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # converting to number
        num1 = self.convert_to_num(l1)
        num2 = self.convert_to_num(l2)
        res = num1 + num2
        new_list = list(map(int, str(res)))
        new_list.reverse()
        obj = ListNode()
        current = obj
        for val in new_list:
            current.next = ListNode(val)
            current = current.next

        return obj.next
        




l1 = [2,4,3]
l2 = [5,6,4]
obj = Solution()
addTwoNumbers = obj.addTwoNumbers(l1,l2)
print(addTwoNumbers)
number = 12345
digits_list = list(map(int, str(number)))
print(digits_list)