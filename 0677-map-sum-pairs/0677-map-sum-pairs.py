class MapSum:

    def __init__(self):
        self.trie = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        if key in self.map:
            n = val - self.map[key]
        else:
            n = val
        for c in key:
            if c not in cur.d:
                cur.d[c] = TrieNode()
            cur.val += n
            cur = cur.d[c]
        cur.val += n
        self.map[key] = val
            
    
    def sum(self, prefix: str) -> int:
        cur = self.trie
        for c in prefix:
            if c not in cur.d:
                return 0
            cur = cur.d[c]
        return cur.val



class TrieNode:
    def __init__(self):
        self.d = {}
        self.val = 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)