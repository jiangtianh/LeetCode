class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = 0
        colors = colors + colors[:k-1]
        print(colors)
        res = 0
        for r in range(1, len(colors)):
            if colors[r] == colors[r-1]:
                l = r
            if r - l + 1 == k:
                res += 1
                l += 1
        
        return res
