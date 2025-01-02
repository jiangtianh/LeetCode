class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        d = collections.defaultdict(set)
        if len(sentence1) != len(sentence2):
            return False

        for x, y in similarPairs:
            d[x].add(y)
            d[y].add(x)
        
        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 == w2:
                continue
            if w2 in d[w1]:
                continue

            return False

        return True