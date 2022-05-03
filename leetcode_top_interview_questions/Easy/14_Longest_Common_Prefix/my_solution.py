class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        len_strs = len(strs)
        if len_strs == 0:
            return res
        len_first_str = len(strs[0])
        for i in range(len_first_str):
            cha = strs[0][i]
            for j in range(1, len_strs):
                if i >= len(strs[j]) or strs[j][i] != cha:
                    return res
            res += cha
        return res