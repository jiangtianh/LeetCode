class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)

        for n in counter:
            if counter[n] % 2 != 0:
                return False
        return True