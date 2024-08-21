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
            li = []
            for i in range(n):
                if i % 2 == 0:
                    li.append(arr[i // 2])
                else:
                    li.append(arr[n // 2 + (i - 1) // 2])
            arr = li
            res += 1
            if check(arr):
                break
        return res