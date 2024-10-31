class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        res = 0
        add = nums[0] + nums[1]
        for i in range(1, len(nums), 2):
            if nums[i] + nums[i-1] == add:
                res += 1
            else:
                break

        return res