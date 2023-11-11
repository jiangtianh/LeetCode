class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def total(divisor):
            res = 0
            for num in nums:
                res += math.ceil(num / divisor)
            return res



        left = 1
        right = max(nums)
        


        while left <= right:
            mid = (left + right) // 2
            val = total(mid)

            if val > threshold:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return left

