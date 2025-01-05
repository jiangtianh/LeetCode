class TrieNode:
    def __init__(self):
        self.d = {}
        self.isContent = False
        self.content = ''


class FileSystem:

    def __init__(self):
        self.head = TrieNode()        

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.head.d.keys())
        path = path[1:].split("/")
        temp = self.head
        for p in path:
            temp = temp.d[p]
        if temp.isContent:
            return [p]
        return sorted(temp.d.keys())

    def mkdir(self, path: str) -> None:
        path = path[1:].split("/")
        temp = self.head
        for p in path:
            if p not in temp.d:
                temp.d[p] = TrieNode()
            temp = temp.d[p]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath[1:].split("/")
        temp = self.head
        for p in path[:-1]:
            temp = temp.d[p]
        if path[-1] not in temp.d:
            temp.d[path[-1]] = TrieNode()
        temp = temp.d[path[-1]]
        temp.isContent = True
        temp.content += content

    def readContentFromFile(self, filePath: str) -> str:
        temp = self.head
        path = filePath[1:].split("/")
        for p in path:
            temp = temp.d[p]
        return temp.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)