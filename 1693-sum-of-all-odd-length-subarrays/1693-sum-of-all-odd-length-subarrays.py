class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0

        for i in range(len(arr)):
            count = 0
            total = 0
            for j in range(i, len(arr)):
                count += 1
                total += arr[j]

                if count % 2 == 1:
                    res += total
        
        return res