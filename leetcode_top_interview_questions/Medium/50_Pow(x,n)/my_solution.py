class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            tmp = helper(x, n//2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * x
        
        res = 1
        if n > 0:
            return helper(x, n)
        elif n < 0:
            return 1 / helper(x, -n)
        else:
            return res