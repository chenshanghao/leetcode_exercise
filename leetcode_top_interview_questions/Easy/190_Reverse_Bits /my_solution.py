class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            n, digit = divmod(n, 2)
            res = res * 2 + digit
        return res
        