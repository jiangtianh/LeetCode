class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        n = len(searchWord)

        for i, word in enumerate(sentence):
            if word[:n] == searchWord:
                return i + 1
        return -1
