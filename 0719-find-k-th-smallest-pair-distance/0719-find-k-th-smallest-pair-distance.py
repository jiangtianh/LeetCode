class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(maxValue):
            count = 0
            l = 0

            for r in range(n):
                while nums[r] - nums[l] > maxValue:
                    l += 1
                count += r - l
            return count 


        low = 0
        high = nums[-1] - nums[0]
        res = math.inf

        while low <= high:
            mid = (low + high) // 2
            c = count(mid)
            if c >= k:
                res = min(res, mid)
                high = mid - 1
            elif c < k:
                low = mid + 1
            
        return res