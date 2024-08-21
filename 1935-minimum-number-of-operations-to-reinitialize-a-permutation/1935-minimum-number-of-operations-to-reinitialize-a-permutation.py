class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = [i for i in range(n)]

        def check(arr):
            for i in range(1,len(arr)):
                if arr[i] != arr[i-1] + 1:
                    return False
            return True 
        res = 0
        while True:
            li = [0 for _ in range(n)]
            for i in range(n):
                if i % 2 == 0:
                    li[i] = (arr[i // 2])
                else:
                    li[i] = (arr[n // 2 + (i - 1) // 2])
            arr = li
            res += 1
            if check(arr):
                break
        return res