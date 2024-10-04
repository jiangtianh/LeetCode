class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        l = 0
        r = n - 1
        i = skill[l] + skill[r]
        res = 0
        while l < r:
            if skill[l] + skill[r] != i:
                return -1
            res += skill[l] * skill[r]
            l += 1
            r -= 1
    
        return res