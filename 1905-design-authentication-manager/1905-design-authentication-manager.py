class Node:
    def __init__(self, val, ):
        self.val = val
        self.exp = 0
        self.prev = None 
        self.next = None

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.head = Node("0")
        self.head.exp = 0
        self.tail = Node("0")
        self.tail.exp = math.inf
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
        self.d = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.deleteTillTime(currentTime)
        if tokenId in self.d:
            return
        newToken = Node(tokenId)
        newToken.exp = currentTime + self.timeToLive
        self.d[tokenId] = newToken
        self.count += 1

        temp = self.tail
        while temp.exp > newToken.exp:
            temp = temp.prev
        nextNode = temp.next
        newToken.prev = temp
        newToken.next = nextNode
        nextNode.prev = newToken
        temp.next = newToken



                

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.deleteTillTime(currentTime)
        if tokenId not in self.d:
            return
        
        token = self.d[tokenId]
        token.exp = currentTime + self.timeToLive
        prevNode = token.prev
        nextNode = token.next
        token.next = None
        token.prev = None
        prevNode.next = nextNode
        nextNode.prev = prevNode

        temp = self.tail
        while temp.exp > token.exp:
            temp = temp.prev
        nextNode = temp.next
        token.prev = temp
        token.next = nextNode
        nextNode.prev = token
        temp.next = token
    
        


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.deleteTillTime(currentTime)
        return self.count



    def deleteTillTime(self, time):
        temp = self.head.next
        while self.count > 0 and temp.exp <= time:
            self.d.pop(temp.val)
            nextNode = temp.next
            self.head.next = nextNode
            nextNode.prev = self.head
            temp = nextNode
            self.count -= 1

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)