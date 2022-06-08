class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n, l, r, tmp, res):
            if l > n or r > n:
                return 
            if r > l:
                return
            if l == n and r == n:
                res.append("".join(tmp))
            

            tmp.append("(")
            helper(n, l+1, r, tmp, res)
            tmp.pop()
            
            tmp.append(")")
            helper(n, l, r+1, tmp, res)
            tmp.pop()
        
        res = []
        helper(n, 0, 0, [], res)
        return res
        