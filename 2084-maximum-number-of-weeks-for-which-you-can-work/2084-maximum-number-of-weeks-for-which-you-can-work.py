class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        n = len(milestones)
        if n == 1:
            return 1
        total = sum(milestones[:-1])
        if milestones[-1] > total + 1:
            return total * 2 + 1
        else:
            return total + milestones[-1]