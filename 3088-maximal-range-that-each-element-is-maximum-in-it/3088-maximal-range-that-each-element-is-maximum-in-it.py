class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * n
        r = [0] * n
        
        stack = []
        for i in range(n):
            num = nums[i]
            while stack and stack[-1][1] < num:
                stack.pop()
            if stack:
                l[i] = i - stack[-1][0] - 1
            else:
                l[i] = i
            stack.append([i, num])
        
        stack = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while stack and stack[-1][1] < num:
                stack.pop()
            if stack:
                r[i] = stack[-1][0] - i - 1
            else:
                r[i] = n - i - 1
            stack.append([i, num])
        
        res = []
        for i in range(n):
            res.append(1 + l[i] + r[i])
        return res