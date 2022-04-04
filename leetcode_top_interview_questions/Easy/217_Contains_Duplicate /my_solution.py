class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(n)
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for k, v in hashmap.items():
            if v > 1:
                return True
        return False