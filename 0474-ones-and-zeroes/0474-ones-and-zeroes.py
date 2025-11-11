class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        count = [[0, 0] for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                if c == "0":
                    count[i][0] += 1
                else:
                    count[i][1] += 1
        
        @cache
        def f(i, zeros, ones):
            if zeros > m or ones > n:
                return -math.inf
            if i == len(strs):
                return 0
            return max(f(i+1, zeros + count[i][0], ones + count[i][1]) + 1, f(i+1, zeros, ones))

        return f(0, 0, 0)