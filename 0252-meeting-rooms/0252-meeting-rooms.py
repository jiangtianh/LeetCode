class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])

        pre = -1
        for start, end in intervals:
            if start >= pre:
                pre = end
            else:
                return False

        return True
