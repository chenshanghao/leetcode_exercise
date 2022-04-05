class Solution:
    def isHappy(self, n: int) -> bool:
        return self.helper(n, {})
        
    def helper(self, n, hashmap):
        if n > pow(2,31) -1:
            return False
        res = 0
        while(n > 0):
            res = res + (n%10) * (n%10)
            n = n//10
        if res == 1:
            return True
        elif res in hashmap:
            return False
        else:
            hashmap[res] = True
            return self.helper(res, hashmap)
        