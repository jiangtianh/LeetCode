class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        prev = nums[0]
        res = 0
        count = 0

        for i in range(1, len(nums)):
            num = nums[i]
            count += 1
            if num != prev:
                
                res += count
                prev = num
            
        return res

