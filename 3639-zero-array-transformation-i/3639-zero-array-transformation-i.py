class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        li = [0] * (n+1)

        for l, r in queries:
            li[l] -= 1
            li[r+1] += 1
        
        print(li)
        current = 0

        for i in range(n):
            current += li[i]
            if nums[i] + current > 0:
                return False
        return True