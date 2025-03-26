class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = []
        left, right = 0, 0
        remainder = grid[0][0] % x
        for row in grid:
            for n in row:
                if n % x != remainder:
                    return -1
                li.append(n)
                right += n
        
        li.sort()
        res = math.inf
        for i, n in enumerate(li):
            right -= n
            leftElement, rightElement = i, len(li) - i - 1
            leftTotal, rightTotal = leftElement * n, rightElement * n
            leftNeed = (leftTotal - left) // x
            rightNeed = (right - rightTotal) // x
            res = min(res, leftNeed + rightNeed)
            left += n
        return res