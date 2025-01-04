"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        temp = head
        if not temp:
            newNode.next = newNode
            return newNode
        elif temp == temp.next:
            newNode.next = temp
            temp.next = newNode
            return head
        notInserted = False 
        while temp:
            if temp.val > temp.next.val:
                if insertVal > temp.val or insertVal < temp.next.val:
                    newNode.next = temp.next
                    temp.next = newNode
                    break
            if temp.val <= insertVal <= temp.next.val:
                newNode.next = temp.next
                temp.next = newNode
                break

            temp = temp.next
            if temp == head:
                notInserted = True
                break

        if notInserted:
            newNode.next = head.next
            head.next = newNode
        
        return head