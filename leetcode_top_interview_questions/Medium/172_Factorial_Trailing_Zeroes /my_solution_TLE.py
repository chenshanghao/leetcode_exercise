class Solution:
    def trailingZeroes(self, n: int) -> int:
        fac_val = 1
        for i in range(1, n+1):
            fac_val = fac_val * i
        
        res = 0
        while fac_val % 10 == 0:
            res += 1
            fac_val = fac_val // 10
        
        return res
        