class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x< 0:
            is_neg = True
            x = x * (-1)
        res = 0
        while True:
            rem = x % 10
            x = x//10
            res = res*10 + rem
            if x == 0:
                break
        if is_neg:
            res = (-1)* res
        return res
    

x = 1534236469
# x = 123
obj = Solution()
result = obj.reverse(x)
print(result)
print(x)
