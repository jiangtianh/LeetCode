class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        temp = self.head 
        
        for i in range(len(word)):
            c = word[i]
            if c not in temp.d:
                temp.d[c] = Node()
            
            temp = temp.d[c]
        temp.isEnd = True
            
            
        

    def search(self, word: str) -> bool:
        temp = self.head
        for i in range(len(word)):
            c = word[i]
            if c not in temp.d:
                return False 
            temp = temp.d[c]
        return temp.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in temp.d:
                return False 
            temp = temp.d[c]
        return True 
        
        

class Node:
    def __init__(self):
        self.d = {}
        self.isEnd = False 
        
        
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)