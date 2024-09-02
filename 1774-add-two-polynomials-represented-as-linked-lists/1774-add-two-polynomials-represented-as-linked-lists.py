# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        
        Sentinal = PolyNode()
        temp = Sentinal

        while poly1 and poly2:
            if poly1.power == poly2.power:
                if poly1.coefficient + poly2.coefficient != 0:
                    temp.next = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    temp = temp.next
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.power > poly2.power:
                if poly1.coefficient != 0:
                    temp.next = PolyNode(poly1.coefficient, poly1.power)
                    temp = temp.next
                poly1 = poly1.next
            else:
                if poly2.coefficient != 0:
                    temp.next = PolyNode(poly2.coefficient, poly2.power)
                    temp = temp.next
                poly2 = poly2.next
            
        while poly1:
            if poly1.coefficient != 0:
                temp.next = PolyNode(poly1.coefficient, poly1.power)
                temp = temp.next
            poly1 = poly1.next
        while poly2:
            if poly2.coefficient != 0:
                temp.next = PolyNode(poly2.coefficient, poly2.power)
                temp = temp.next
            poly2 = poly2.next
            

        return Sentinal.next