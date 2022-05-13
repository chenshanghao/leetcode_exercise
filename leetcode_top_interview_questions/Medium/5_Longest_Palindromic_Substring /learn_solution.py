class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r):
            n = len(s)
            while l >= 0 and r <= n -1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        res = ""
        max_length = 0
        
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            if len(helper(s, i, i)) > len(res):
                res = helper(s, i, i)
            if i > 0 and len(helper(s, i-1, i)) > len(res):
                res = helper(s, i-1, i)
        return res
        