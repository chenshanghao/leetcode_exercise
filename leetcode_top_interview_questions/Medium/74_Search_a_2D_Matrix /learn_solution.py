class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
                
        if matrix[mid][0] > target or matrix[mid][-1] < target:
            return False
        
        search_list = matrix[mid]
        l, r = 0, len(search_list) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if search_list[mid] == target:
                return True
            elif search_list[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return True if search_list[mid] == target else False
            