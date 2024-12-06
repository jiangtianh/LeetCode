class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res = 0
        count = 0
        for i in range(1, n+1):
            if i in banned:
                continue 
            
            if res + i > maxSum:
                break
            else:
                res += i
                count += 1

        return count 