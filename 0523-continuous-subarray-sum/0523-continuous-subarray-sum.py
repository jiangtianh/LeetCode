class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        total = 0

        for i, n in enumerate(nums):
            total += n
            remainder = total % k
            if remainder == 0 and i != 0:
                return True 
            if remainder in d:
                if i - d[remainder] > 1:
                    return True
            else:
                d[remainder] = i

        return False