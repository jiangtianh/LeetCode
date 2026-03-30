class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        oddC = collections.defaultdict(int)
        evenC = collections.defaultdict(int)

        oddC2 = collections.defaultdict(int)
        evenC2 = collections.defaultdict(int)

        for i in range(len(s1)):
            if i % 2 == 0:
                evenC[s1[i]] += 1
                evenC2[s2[i]] += 1
            else:
                oddC[s1[i]] += 1
                oddC2[s2[i]] += 1

        return oddC == oddC2 and evenC == evenC2