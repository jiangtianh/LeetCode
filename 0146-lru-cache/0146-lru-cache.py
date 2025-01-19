class Node:
    def __init__(self, n=0, key=0):
        self.prev = None
        self.key = key
        self.val = n
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head  
        self.d = {}      
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1 
        
        self.moveToFront(key)
        return self.d[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            newNode = Node(value, key)
            self.d[key] = newNode
            
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next.prev = newNode
            self.head.next = newNode

            self.size += 1
            self.cleanup()

        else:
            self.d[key].val = value
            self.moveToFront(key)


    def moveToFront(self, key):
        node = self.d[key]
        prevNode = node.prev
        nextnode = node.next
        node.prev = None 
        node.next = None
        prevNode.next = nextnode
        nextnode.prev = prevNode

        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    def cleanup(self):
        while self.size > self.capacity:
            lastNode = self.tail.prev
            self.d.pop(lastNode.key)
            newTail = lastNode.prev 
            newTail.next = self.tail
            self.tail.prev = newTail

            self.size -= 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)