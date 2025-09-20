class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for n in range(numRows):
            row = [1] * (n + 1)
            for j in range(1,n):
                row[j] = res[n-1][j-1] + res[n-1][j]
            res.append(row)
        return res