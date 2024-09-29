class Node:
    def __init__(self):
        self.char = {}
        self.isEnd = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        tempNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in tempNode.char:
                newNode = Node() 
                tempNode.char[c] = newNode 
    
            tempNode = tempNode.char[c]
        tempNode.isEnd = True 
        tempNode.count += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        count = 0 
        tempNode = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in tempNode.char:
                return 0 
            tempNode = tempNode.char[c]
        return tempNode.count
        

    def countWordsStartingWith(self, prefix: str) -> int:
        self.res = 0
        def count(node):
            if node.isEnd:
                self.res += node.count 
            for char in node.char:
                count(node.char[char])

        tempNode = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in tempNode.char:
                return 0 
            tempNode = tempNode.char[c]
        count(tempNode)
        return self.res






    def erase(self, word: str) -> None:
        tempNode = self.root
        for i in range(len(word)):
            c = word[i]
            tempNode = tempNode.char[c]
        tempNode.count -= 1



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

