class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(key= lambda x: x[0], reverse=True)

        stack = []
        
        for pos, speed in cars:
            time = (target - pos) / speed

            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
            
            
                
                

