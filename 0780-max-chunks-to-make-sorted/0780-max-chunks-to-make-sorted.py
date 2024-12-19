class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        total = 0
        actual = 0

        for i in range(len(arr)):
            total += i
            actual += arr[i]
            if total == actual:
                res += 1
        
        return res
