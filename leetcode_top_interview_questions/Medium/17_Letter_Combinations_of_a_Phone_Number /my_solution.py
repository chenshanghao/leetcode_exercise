class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        hashmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        def helper(hashmap, res, digits, tmp):
            if len(digits) == len(tmp):
                res.append(tmp)
            else:
                idx = len(tmp)
                char = int(digits[idx])
                for s in hashmap[char]:
                    helper(hashmap, res, digits, tmp + s)
            return res
        
        res = helper(hashmap, [], digits, '')
        return res
                