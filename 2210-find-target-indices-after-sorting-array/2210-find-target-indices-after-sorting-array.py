class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n == target:
                res.append(i)   

            elif n > target:
                break

        return res