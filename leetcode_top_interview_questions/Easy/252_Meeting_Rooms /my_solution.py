class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals)
        cur = intervals[0]
        for interval in intervals[1:]:
            if cur[1] > interval[0]:
                return False
            cur = interval
            
        return True
        