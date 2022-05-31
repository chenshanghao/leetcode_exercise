class Solution:
    def fib(self, n: int) -> int:
        hashmap = {}
        def helper(n):
            if n in hashmap:
                return hashmap[n]
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return helper(n-1) + helper(n-2)
        return helper(n)
        