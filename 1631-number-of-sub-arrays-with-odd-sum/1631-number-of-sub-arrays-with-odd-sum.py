class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount = 0
        evenCount = 0

        total = 0
        res = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                res += oddCount
                evenCount += 1
            else:
                res += 1
                res += evenCount
                oddCount += 1
                

        return res % (10 ** 9 + 7)