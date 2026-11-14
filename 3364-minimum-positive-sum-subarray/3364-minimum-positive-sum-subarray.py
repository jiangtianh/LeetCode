class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
    
        # Check every allowed subarray length k
        for k in range(l, r + 1):
            # Calculate sum of the first window of size k
            current_sum = sum(nums[:k])
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)
                
            # Slide the window of size k across the array
            for i in range(k, len(nums)):
                current_sum += nums[i] - nums[i - k]
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1