class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        def twosum(l, r, target):
            res = []
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            return res
        

        def kSum(k, start, target):
            if k == 2:
                return twosum(start, len(nums)-1, target)
                
            temp = []
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                num = nums[i]
                
                res = kSum(k - 1, i+1, target - num)
                for li in res:
                    temp.append([num] + li)

            return temp

        return kSum(4, 0, target)