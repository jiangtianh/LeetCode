class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            shorter = sentence1
            longer = sentence2
        else:
            shorter = sentence2
            longer = sentence1
        longer = longer.split(' ')
        shorter = shorter.split(' ')
        n, m = len(shorter), len(longer)

    
        longestPrefix = 0
        for i in range(min(n, m)):
            if shorter[i] == longer[i]:
                longestPrefix += 1
            else:
                break

        i, j = n-1, m-1
        longestSuffix = 0
        while i >= longestPrefix and shorter[i] == longer[j]:
            longestSuffix += 1            
            i -= 1
            j -= 1
        
        return longestPrefix + longestSuffix == n
            