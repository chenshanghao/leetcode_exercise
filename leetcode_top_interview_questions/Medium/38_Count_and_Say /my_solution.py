class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(n):
            s = str(n)
            last_seen_char = s[0]
            cnt = 1
            res = ''
            for i in range(1, len(s)):
                if s[i] == last_seen_char:
                    cnt += 1
                else:
                    res = res + str(cnt) + last_seen_char
                    cnt = 1
                    last_seen_char = s[i]
            
            res = res + str(cnt) + last_seen_char
            return res
        
        res = 1
        for i in range(n-1):
            res = helper(res)
        return str(res)