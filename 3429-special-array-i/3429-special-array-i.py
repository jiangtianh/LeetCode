class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0] % 2

        for i in range(1, len(nums)):
            parity = nums[i] % 2
            if parity == prev:
                return False
            prev = parity

        return True