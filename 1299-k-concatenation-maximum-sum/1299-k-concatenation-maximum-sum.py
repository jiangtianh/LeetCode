class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        cur = 0
        k1Res = 0
        for n in arr:
            cur += n
            if cur < 0:
                cur = 0
            k1Res = max(k1Res, cur)
        if k == 1:
            return k1Res
        total = sum(arr)
        cur = 0
        left = 0
        for n in arr:
            cur += n
            left = max(left, cur)
        right = 0
        cur = 0
        for i in range(len(arr)-1, -1, -1):
            cur += arr[i]
            right = max(right, cur)

        
        leftAndRight = left + right
        res = (left + right + (total * (k-2)))

        finalRes = max(res, leftAndRight, k1Res)

        return finalRes % (10 ** 9 + 7)