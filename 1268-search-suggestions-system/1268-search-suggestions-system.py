class Node:
    def __init__(self):
        self.isEnd = False 
        self.children = [None] * 26
        

class Trie:
    def __init__(self):
        self.head = Node() 
        
    def add(self, word):
        curr = self.head
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = Node()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEnd = True        
    
    
                
    def search(self, prefix):
        
        def dfs(node, word):
            if len(res) == 3:
                return;
            if node.isEnd:
                res.append(word)

            for i in range(0, 26):
                if node.children[i]:
                    dfs(node.children[i], word + chr(i + ord('a')))
        
        curr = self.head
        res = []
        for c in prefix:
            if not curr.children[ord(c) - ord('a')]:
                return res
            curr = curr.children[ord(c) - ord('a')]
        dfs(curr, prefix)
        return res
    
    
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        result = []
        
        for s in products:
            trie.add(s)
        
        word = ""
        for c in searchWord:
            word += c
            result.append(trie.search(word))
        
        return result
        
        
        
        