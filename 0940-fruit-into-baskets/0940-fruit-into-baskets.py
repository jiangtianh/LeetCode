class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        res = 0

        l = 0
        for r, fruit in enumerate(fruits):
            d[fruit] = d.get(fruit, 0) + 1
            while l < r and len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res