class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}
        for word in wordDict:
            hashmap[word] = True
            
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            if s[0:i] in hashmap:
                dp[i] = True
                continue
            
            for word in hashmap:
                if i - len(word) >= 0 and s[i-len(word): i] == word and dp[i - len(word)]:
                    dp[i] = True
        return dp[-1]