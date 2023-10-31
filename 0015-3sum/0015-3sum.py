class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 

        res = []
        for i in range(len(nums)):
            num = nums[i]
            if i != 0 and num == nums[i - 1]:
                continue

            if num > 0:
                break 

            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + num == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l +=1 
                elif nums[l] + nums[r] + num > 0:
                    r -= 1
                else: 
                    l += 1

        return res

            