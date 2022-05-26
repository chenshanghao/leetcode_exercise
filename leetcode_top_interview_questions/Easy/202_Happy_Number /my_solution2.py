class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        res = None
        while n not in hashmap:
            hashmap[n] = True
            res = 0
            while n > 0:
                v = n % 10
                n = n // 10
                res += v * v
            if res == 1:
                return True
            n = res
        return False
        