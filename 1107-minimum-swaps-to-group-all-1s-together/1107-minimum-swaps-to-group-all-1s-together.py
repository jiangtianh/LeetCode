class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l = 0
        totalOne = data.count(1)
        res = math.inf
        zeroCount = 0

        if totalOne == 0:
            return 0

        for r, num in enumerate(data):
            if num == 0:
                zeroCount += 1
            
            if r - l + 1 == totalOne:
                res = min(res, zeroCount)

                if data[l] == 0:
                    zeroCount -= 1          
                l += 1

        return res