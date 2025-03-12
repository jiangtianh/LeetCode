class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        leftMost = min(right) if right else -1
        rightMost = max(left) if left else -1

        if leftMost == -1:
            return rightMost
        elif rightMost == -1:
            return n - leftMost
        return max(rightMost, n - leftMost)