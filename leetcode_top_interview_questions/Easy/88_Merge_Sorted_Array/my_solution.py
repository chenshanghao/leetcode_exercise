class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        i = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 = p1 -1
            else:
                nums1[i] = nums2[p2]
                p2 = p2 -1
            i = i - 1
        if p2 >= 0:
            for idx in range(p2, -1, -1):
                nums1[idx] = nums2[p2]
                p2 = p2 -1 
            