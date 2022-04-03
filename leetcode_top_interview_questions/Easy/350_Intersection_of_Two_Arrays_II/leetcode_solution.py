# Time Complexity: O(nlogn+mlogm)
# Space Complexity: O(n+m)

class Solution(object):
    def intersect(self, nums1, nums2):
        n1, n2, res = sorted(nums1), sorted(nums2), []
        p1 = p2 = 0
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] < n2[p2]:
                p1 += 1
            elif n2[p2] < n1[p1]:
                p2 += 1
            else:
                res.append(n1[p1])
                p1 += 1
                p2 += 1
        return res


# Time Complexity O(m+n)
# Space Complexity O(min(n, m))
class Solution(object):
    def intersect(self, nums1, nums2):
        # If nums1 is larger than nums2, swap the arrays.
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res