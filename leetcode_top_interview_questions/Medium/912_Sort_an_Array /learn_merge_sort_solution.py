class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            pivot = len(nums) // 2
            left_list = merge_sort(nums[0:pivot])
            right_list = merge_sort(nums[pivot:])
            return merge(left_list, right_list)
        
        def merge(left_list, right_list):
            l_idx, r_idx = 0, 0
            ret = []
            while l_idx < len(left_list) and r_idx < len(right_list):
                if left_list[l_idx] < right_list[r_idx]:
                    ret.append(left_list[l_idx])
                    l_idx += 1
                else:
                    ret.append(right_list[r_idx])
                    r_idx += 1
            
            if l_idx < len(left_list):
                ret.extend(left_list[l_idx:])
            
            if r_idx < len(right_list):
                ret.extend(right_list[r_idx:])
            return ret
        return merge_sort(nums)