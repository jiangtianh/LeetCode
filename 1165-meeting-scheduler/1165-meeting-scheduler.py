class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        
        idx1, idx2 = 0, 0
        
        while idx1 < len(slots1) and idx2 < len(slots2):
            p1Start, p1End = slots1[idx1]
            p2Start, p2End = slots2[idx2]

            if p1End < p2Start:
                idx1 += 1
            elif p2End < p1Start:
                idx2 += 1
            else:
                startTime = max(p1Start, p2Start)
                endTime = min(p1End, p2End)
                timsInCommon = endTime - startTime

                if timsInCommon >= duration:
                    return [startTime, startTime + duration]

                if p2End < p1End:
                    idx2 += 1
                else:
                    idx1 += 1

        
        return []