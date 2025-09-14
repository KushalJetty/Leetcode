class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            reversed_int = int(str(x)[::-1])
            print(reversed_int)
            if x == reversed_int:
                return True
            else:
                return False
        else:
            return False
        
obj = Solution()
x = 313
print(obj.isPalindrome(x))