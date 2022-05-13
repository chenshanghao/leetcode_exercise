class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 1
        hashmap = {}
        l = 0
        hashmap[s[0]] = 0
        for i in range(1, len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
                res = max(res, i - l + 1)
            else:
                if hashmap[s[i]] < l:
                    res = max(res, i - l + 1)
                    hashmap[s[i]] = i
                else:
                    l = hashmap[s[i]] + 1
                    hashmap[s[i]] = i
        return res
        