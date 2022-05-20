class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, res, s, n):
            if len(s) == n*2:
                res.append(s)
                
            if left < n:
                helper(left+1, right, res, s+'(', n)
                
            if right < left:
                helper(left, right+1, res, s+')', n)
            return res
            
        res = helper(0, 0, [], "", n)
        return res