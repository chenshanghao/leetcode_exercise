class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals) <= 1:
            return intervals
        res = []
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] < interval[0]:
                res.append(cur)
                cur = interval
            else:
                cur = [cur[0], max(cur[1], interval[1])]
        res.append(cur)
        return res

        