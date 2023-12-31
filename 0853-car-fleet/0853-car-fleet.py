class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for pos, speed in cars:
            timeToDestination = (target - pos) / speed
            
            if stack and timeToDestination <= stack[-1]:
                continue 
            else:
                stack.append(timeToDestination)
                
        return len(stack)
        
        