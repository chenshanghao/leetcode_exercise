class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_char_count = {}
        length = len(s)
        
        # build the hashmap; character and how often if appears
        for char in s:
            if char in dict_char_count:
                dict_char_count[char] += 1
            else:
                dict_char_count[char] = 1
                
        # find the index
        for i in range(length):
            if dict_char_count[s[i]] == 1:
                return i
        return -1