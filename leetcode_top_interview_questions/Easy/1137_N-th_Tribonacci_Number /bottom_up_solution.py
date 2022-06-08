class Solution:
    def tribonacci(self, n: int) -> int:
        # T0 = 0
        # T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        res = [0, 1, 1]
        for i in range(3, n+1):
            res.append(res[i-1] + res[i-2] + res[i-3])
        
        return res[n]

