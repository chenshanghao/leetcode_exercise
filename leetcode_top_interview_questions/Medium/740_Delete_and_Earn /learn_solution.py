class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        max_number = 0
        
        # precompute how many points we gain from taking an element
        for num in nums:
            points[num] = points.get(num, 0) + num
            max_number = max(max_number, num)
            
        # Base case
        two_back = 0
        one_back = points.get(1, 0)
        
        for num in range(2, max_number + 1):
            two_back, one_back = one_back, max(two_back + points.get(num, 0), one_back)
        return one_back