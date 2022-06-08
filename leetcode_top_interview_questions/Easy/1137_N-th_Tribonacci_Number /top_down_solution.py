class Solution:
    def tribonacci(self, n: int) -> int:
        hashmap = {0:0, 1:1, 2:1}
        def calc(n):
            if n in hashmap:
                return hashmap[n]
            
            return calc(n-1) + calc(n-2) + calc(n-3)
        
        return calc(n)