class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}
        for word in wordDict:
            hashmap[word] = True
        for i in range(len(s)):
            for word in hashmap:
                if i >= len(word):
                    if s[i+1-len(word): i+1]==word and s[0:i+1-len(word)] in hashmap:
                        hashmap[s[0:i+1]] = True
                        break
        return s in hashmap
                        