class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while(n > 0):
            n, digit = divmod(n, 2)
            if digit == 1:
                res += 1
        return res
            