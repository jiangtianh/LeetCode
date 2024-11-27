class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutesDegree = 6 * minutes
        hourDegree = (hour % 12) * 30 + (minutes / 60) * 30

        print("minutes: ", minutes)
        print("hours: ", hourDegree)
        
        diff = abs(hourDegree - minutesDegree)
        print("diff: ", diff)
        return min(diff, 360 - diff)