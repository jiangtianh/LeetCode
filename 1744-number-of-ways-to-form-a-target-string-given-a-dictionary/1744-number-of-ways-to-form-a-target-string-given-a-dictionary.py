class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wordLength = len(words[0])
        targetLength = len(target)
        counter = [collections.defaultdict(int) for _ in range(wordLength)]
        for word in words:
            for i, c in enumerate(word):
                counter[i][c] += 1
        
        @cache
        def f(wordI, targetI):
            if targetI == targetLength:
                return 1
            elif wordI == wordLength:
                return 0
            c = target[targetI]
            if c in counter[wordI]:
                occurances = counter[wordI][c]
                res = f(wordI+1, targetI) + f(wordI+1, targetI+1) * occurances
            else:
                res = f(wordI+1, targetI)
            return res % (10 ** 9 + 7)
        
        return f(0, 0)