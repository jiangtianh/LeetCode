class TrieNode:
    def __init__(self):
        self.d = {}
        self.isEnd = False
        self.heat = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.head = TrieNode()

        for sentence, time in zip(sentences, times):
            cur = self.head
            for c in sentence:
                if c not in cur.d:
                    cur.d[c] = TrieNode()
                cur = cur.d[c]
            cur.isEnd = True
            cur.heat = time
        
        self.prefix = []
        self.cur = self.head
        

    def input(self, c: str) -> List[str]:
        if c == "#":

            temp = self.head
            for c in self.prefix:
                if c not in temp.d:
                    temp.d[c] = TrieNode()
                temp = temp.d[c]
            temp.isEnd = True
            temp.heat += 1

            self.cur = self.head
            self.prefix = []
            return []
        if not self.cur: 
            self.prefix.append(c)
            return []
        self.prefix.append(c)
        self.cur = self.cur.d.get(c)
        if self.cur is None:
            return []

        li = []
        cur = self.cur
        temp = []
        def traverse(cur):
            if cur.isEnd:
                li.append((-cur.heat, "".join(temp)))
            for char in cur.d:
                temp.append(char)
                traverse(cur.d[char])
                temp.pop()
        traverse(cur)
        heapq.heapify(li)
        res = []
        for _ in range(3):
            if not li:
                return res
            _, suffix = heapq.heappop(li)
            res.append("".join(self.prefix) + suffix)
        
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)