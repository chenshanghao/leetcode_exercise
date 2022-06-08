class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(n, k, tmp, cur, res):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            
            for i in range(cur, n + 1):
                tmp.append(i)
                helper(n, k, tmp, i+1, res)
                tmp.pop()
        res = []
        helper(n, k, [], 1, res)
        
        return res