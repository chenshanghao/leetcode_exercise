class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(n-1, -1, -1):
            res += (ord(columnTitle[i]) - ord("A") + 1) * pow(26, n-1-i)
            
        return res
            
        