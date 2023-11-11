class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        temp = 0
        for i, num in enumerate(nums):
            temp += num
            nums[i] = temp
        print(nums)

        for n in queries:
            l = 0 
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= n:
                    l = m + 1
                else:
                    r = m - 1
            res.append(l)
        
        return res


