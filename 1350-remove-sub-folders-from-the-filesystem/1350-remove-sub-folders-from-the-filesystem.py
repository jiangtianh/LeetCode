class TrieNode:
    def __init__(self):
        self.d = {}
        self.isEnd = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = TrieNode()
        folder.sort()
        res = []


        def f(path):
            cur = trie
            
            for p in path.split("/")[1:]:
                if p not in cur.d:
                    cur.d[p] = TrieNode()
                else:
                    if cur.d[p].isEnd:
                        return 
                cur = cur.d[p]
            cur.isEnd = True
            res.append(path)
        
        for path in folder:
            f(path)
        return res