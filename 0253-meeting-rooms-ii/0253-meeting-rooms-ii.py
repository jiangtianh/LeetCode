class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
    
        endTime = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            flip = False
            for j, t in enumerate(endTime):
                if start >= t:
                    endTime[j] = intervals[i][1]
                    flip = True 
                    break
            
            if not flip:
                endTime.append(intervals[i][1])
            
        return len(endTime)
                    
                    
        
        
    
                    