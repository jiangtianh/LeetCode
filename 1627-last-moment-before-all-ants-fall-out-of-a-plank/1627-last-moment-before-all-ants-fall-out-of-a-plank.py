class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        leftMost = 0
        rightMost = 0

        if left:
            leftMost = max(left)
            
        if right:
            
            rightMost = n - min(right)
       
        if leftMost and rightMost:
            print("111")
            return max(leftMost, rightMost)
        elif leftMost:
            return leftMost 
        else:
            return rightMost
        


