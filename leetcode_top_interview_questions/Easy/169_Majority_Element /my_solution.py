class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = float('inf')
        cnt = 0
        
        for num in nums:
            if num == res:
                cnt += 1
            else:
                if cnt == 0:
                    res = num
                    cnt = 1
                else:
                    cnt -= 1
        return res

        