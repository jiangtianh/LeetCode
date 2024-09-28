class Node:
    def __init__(self, n):
        self.val = n
        self.next = None 
        self.prev = None 



class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.front = None 
        self.end = None 

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.front = Node(value)
            self.end = self.front
            self.size += 1
            return True 
        elif self.isFull():
            return False
        else:
            newNode = Node(value)
            self.front.prev = newNode
            newNode.next = self.front
            self.front = newNode
            self.size += 1
            return True 


    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.front = Node(value)
            self.end = self.front
            self.size += 1
            return True 
        elif self.isFull():
            return False
        else:
            newNode = Node(value)
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
            self.size += 1
            return True 
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        newFront = self.front.next
        self.front.next = None 
        if newFront:
            newFront.prev = None
        self.front = newFront
        self.size -= 1
        if self.size == 0:
            self.end = None
        return True 

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        newEnd = self.end.prev
        self.end.prev = None 
        if newEnd:
            newEnd.next = None 
        self.end = newEnd
        self.size -= 1
        if self.size == 0:
            self.front = None
        return True

    def getFront(self) -> int:
        return self.front.val if self.front else -1
        

    def getRear(self) -> int:
        return self.end.val if self.end else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()