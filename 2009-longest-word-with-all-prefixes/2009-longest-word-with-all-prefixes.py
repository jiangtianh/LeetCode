class TrieNode:
    def __init__(self):
        self.isWord = False
        self.d = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        temp = self.root
        for c in word:
            if c not in temp.d:
                temp.d[c] = TrieNode()
            temp = temp.d[c]
        temp.isWord = True

    def find(self):
        res = collections.defaultdict(list)
        tempstr = []
        def f(node, level):
            if not node == self.root and not node.isWord:
                return 
            else:
                res[level].append(''.join(tempstr))
                for c in node.d:
                    tempstr.append(c)
                    f(node.d[c], level+1)
                    tempstr.pop()
        f(self.root, 0)
        return res



class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.add(word)

        res = trie.find()

        longest = res[max(res.keys())]

        if not longest:
            return ''
        longest.sort()
        return longest[0]
        
