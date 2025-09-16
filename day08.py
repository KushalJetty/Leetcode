class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        combined_number = int("".join(map(str, digits)))
        combined_number = combined_number + 1
        res = [int(d) for d in str(combined_number)]
        return res