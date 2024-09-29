class Node:
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.prev = None
        self.keys = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)  # Dummy head node with freq 0
        self.tail = self.head  # Initially, head and tail are the same
        self.map = {}  # To store the key -> node mapping


    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)
            
            # Find the next node or create a new one
            nextNode = node.next
            if not nextNode or nextNode.freq != freq + 1:
                newNode = Node(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                if nextNode:
                    nextNode.prev = newNode
                node.next = newNode
                self.map[key] = newNode
                if node == self.tail:
                    self.tail = newNode
            else:
                nextNode.keys.add(key)
                self.map[key] = nextNode

            # Remove the old node if it's empty
            if not node.keys:
                self._removeNode(node)
        else:
            # First time seeing this key, add it to the node with freq 1
            firstNode = self.head.next
            if not firstNode or firstNode.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                if firstNode:
                    firstNode.prev = newNode
                self.head.next = newNode
                self.map[key] = newNode
                if self.tail == self.head:
                    self.tail = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode


    def dec(self, key: str) -> None:
        if key not in self.map:
            return 
        
        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            del self.map[key]
            if not node.keys:
                self._removeNode(node)
            return

        # Find the previous node or create a new one
        prevNode = node.prev
        if prevNode == self.head or prevNode.freq != freq - 1:
            newNode = Node(freq - 1)
            newNode.keys.add(key)
            newNode.prev = prevNode
            newNode.next = node
            prevNode.next = newNode
            node.prev = newNode
            self.map[key] = newNode
            if node == self.head.next:
                self.head.next = newNode
        else:
            prevNode.keys.add(key)
            self.map[key] = prevNode

        # Remove the old node if it's empty
        if not node.keys:
            self._removeNode(node)


    def getMaxKey(self) -> str:
        if self.tail != self.head:
            return next(iter(self.tail.keys))  # Get any key from the set
        return ""


    def getMinKey(self) -> str:
        if self.head.next:
            return next(iter(self.head.next.keys))  # Get any key from the set
        return ""

    
    def _removeNode(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode
        if node == self.tail:
            self.tail = prevNode
