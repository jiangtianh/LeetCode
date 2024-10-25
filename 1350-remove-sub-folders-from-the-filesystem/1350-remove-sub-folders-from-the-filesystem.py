class TrieNode:
    def __init__(self):
        self.d = {}
        self.isEnd = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))

        Trie = TrieNode()
        self.res = []
        def f(path):
            originalPath = path
            path = path[1:].split("/")
            temp = Trie
            for c in path:
                if c not in temp.d:
                    temp.d[c] = TrieNode()
                else:
                    if temp.d[c].isEnd == True:
                        return
                temp = temp.d[c]
            temp.isEnd = True
            self.res.append(originalPath)
        
        for path in folder:
            f(path)
        return self.res
