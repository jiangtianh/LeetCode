
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        indexes = [0]
        

        i = 1

        while i < len(nums):
            if nums[i] % 2 == nums[i-1] % 2:
                indexes.append(i-1)
                indexes.append(i)
            i += 1
        indexes.append(len(nums) - 1)

        res = []

        for _from, _to in queries:
            if _from == _to:
                res.append(True)
                continue

            startIdx = bisect_left(indexes, _from)

            left = startIdx if startIdx % 2 == 0 else startIdx - 1
            right = left + 1

            if _from >= indexes[left] and _to <= indexes[right]:
                res.append(True)
            else:
                res.append(False)

        return res