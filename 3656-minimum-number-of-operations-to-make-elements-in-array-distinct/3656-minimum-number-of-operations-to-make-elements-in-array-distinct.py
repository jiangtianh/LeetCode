class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = len(nums) - 1
        s = set()
        
        while i >= 0:
            num = nums[i]
            if num in s:
                break
            s.add(num)
            i -= 1

        return math.ceil((i+1) / 3)
        