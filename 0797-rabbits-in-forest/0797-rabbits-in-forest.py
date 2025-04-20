class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        counter = collections.Counter(answers)

        for other in counter:
            count = counter[other]
            while count > 0:
                res += other + 1
                count -= other + 1
        
        return res