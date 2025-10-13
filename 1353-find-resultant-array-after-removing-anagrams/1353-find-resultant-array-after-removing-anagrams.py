class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        wordToAnagram = {}
        for word in words:
            wordToAnagram[word] = ''.join(sorted(list(word)))

        
        s = []

        for word in words:
            if s and wordToAnagram[s[-1]] == wordToAnagram[word]:
                continue
            else:
                s.append(word)
            
        return s