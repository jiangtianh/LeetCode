class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        fc = sentence[0][0]
        lc = sentence[-1][-1]

        for word in sentence:
            fc = word[0]

            if fc != lc:
                return False
            lc = word[-1]
        
        return True
