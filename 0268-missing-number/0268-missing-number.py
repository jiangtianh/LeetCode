class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set() 
        for i in range(len(nums) + 1):
            s.add(i)

        for num in nums:
            s.remove(num)

        return list(s)[0]