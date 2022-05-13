class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        cur_idx = 0
        hashmap = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hashmap:
                res[hashmap[sorted_string]].append(string)
            else:
                res.append([string])
                hashmap[sorted_string] = cur_idx
                cur_idx += 1
        return res
            