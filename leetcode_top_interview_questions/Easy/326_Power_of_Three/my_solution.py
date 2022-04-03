class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        num = 1
        while(num <= n):
            if num == n:
                return True
            num *= 3
        return False
        