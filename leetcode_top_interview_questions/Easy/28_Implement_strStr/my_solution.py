class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack, len_needle = len(haystack), len(needle)
        res = -1
        if len_haystack < len_needle:
            return res
        
        for i in range(len_haystack):
            if haystack[i] == needle[0]:
                if haystack[i: i + len_needle] == needle:
                    res = i
                    break
        return res
                