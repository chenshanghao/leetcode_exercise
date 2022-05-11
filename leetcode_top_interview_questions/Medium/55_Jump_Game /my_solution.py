class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hashmap = {}
        hashmap[0] = True
        length = len(nums)
        for i, num in enumerate(nums):
            if i in hashmap:
                for j in range(1, num + 1):
                    hashmap[i + j] = True
                if (length - 1) in hashmap:
                    return True
        
        return False
        
        
            