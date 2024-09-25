class TrieNode: 
    def __init__(self):
        self.d = {}
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        temp = self.root
        for c in word:
            if c not in temp.d:
                temp.d[c] = TrieNode()
            temp = temp.d[c]
            temp.score += 1
    
    def search(self, word):
        temp = self.root
        res = 0
        for c in word:
            temp = temp.d[c]
            res += temp.score
        return res


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()

        for word in words:
            trie.add(word)
        
        res = [0] * len(words)

        for i, word in enumerate(words):
            res[i] = trie.search(word)
        
        return res