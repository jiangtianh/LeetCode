class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = collections.defaultdict(int)
        for word in words2:
            tempCounter = collections.Counter(word)
            for c in tempCounter:
                if tempCounter[c] > counter[c]:
                    counter[c] = tempCounter[c]
        res = []
        print(counter)
        for word in words1:
            tempCounter = collections.Counter(word)
            t = True
            for c in counter:
                if tempCounter[c] < counter[c]:
                    t = False
                    break
            if t:
                res.append(word)
    
        return res