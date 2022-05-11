class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        if len(intervals) < 1:
            return res
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if right >= intervals[i][0]:
                right = max(right,intervals[i][1])
            else:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        res.append([left, right])
        return res
        