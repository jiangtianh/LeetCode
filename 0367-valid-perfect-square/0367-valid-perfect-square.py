class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = sqrt(num)
        return int(res) == res