class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法的关键在于取中间值后，与目标值比较，判断左半段还是右半段。
        # 观察上述八种情况，可以发现以中间值为界，左右两部分总有一段是绝对升序的。
        # 当 nums[mid] < nums[right] 时，右半段绝对升序；
        # 当 nums[mid] > nums[right] 时，左半段绝对升序
        l, r = 0, len(nums) - 1
        while l<r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        print("l:" + str(l) + " r:" + str(r) )
        return -1 if nums[l] != target else l
                    
                    