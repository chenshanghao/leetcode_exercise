class Solution:
    def climbStairs(self, n: int) -> int:
        l1, l2 = 1, 2
        if n == 1:
            return l1
        for idx in range(n - 2):
            new = l1 + l2
            l1 = l2
            l2 = new
        return l2